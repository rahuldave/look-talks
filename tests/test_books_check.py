"""Tests for scripts/books_check.py. Each test makes a new Git repository in a temporary folder."""

import os
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "books_check.py"


class BooksCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "Test")

    def tearDown(self):
        self.tmp.cleanup()

    def git(self, *args):
        subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def add(self, name, content=b"text\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        self.git("add", "-f", name)

    def run_check(self, *args, cwd=None):
        return subprocess.run([sys.executable, "-I", str(SCRIPT), *args], cwd=cwd or self.root,
                              capture_output=True).returncode

    def large_file_setup(self, listed_content, staged_content, stage_list=True, commit=False):
        """Stage a large-files list and one large file, then run the check with --history.

        With commit=True, the files are committed and the index is emptied of them, so that only the history
        path of the check can see them."""
        sha = subprocess.run(["git", "hash-object", "--stdin"], input=listed_content, capture_output=True,
                             check=True).stdout.decode().strip()
        (self.root / "scripts").mkdir()
        (self.root / "scripts" / "large-files.txt").write_text(f"# reviewed\n{sha} theme.scss\n")
        if stage_list:
            self.git("add", "-f", "scripts/large-files.txt")
        self.add("theme.scss", staged_content)
        if commit:
            self.git("commit", "-q", "-m", "x")
            self.git("rm", "-q", "--cached", "theme.scss")
        return self.run_check("--history")

    def test_a_listed_large_file_passes(self):
        content = b"/* theme */\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(content, content), 0)

    def test_a_changed_large_file_fails(self):
        content = b"/* theme */\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(content, content + b"b"), 1)

    def test_a_listed_large_pdf_still_fails(self):
        content = b"%PDF-1.7\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(content, content), 1)

    def test_a_list_that_is_not_staged_allows_nothing(self):
        content = b"/* theme */\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(content, content, stage_list=False), 1)

    def test_the_history_path_uses_the_list(self):
        content = b"/* theme */\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(content, content, commit=True), 0)

    def test_the_history_path_fails_an_unlisted_large_file(self):
        listed = b"/* other */\n" + b"a" * (1024 * 1024 + 10)
        content = b"/* theme */\n" + b"a" * (1024 * 1024 + 10)
        self.assertEqual(self.large_file_setup(listed, content, commit=True), 1)

    def test_clean_repository_passes(self):
        self.add("README.md")
        self.assertEqual(self.run_check(), 0)

    def test_pdf_and_books_folder_fail(self):
        for name in ("a.pdf", "b.PDF", "books/notes.md", "sub/Books/x.txt"):
            with self.subTest(name=name):
                self.git("rm", "-rq", "--cached", "--ignore-unmatch", ".")
                self.add(name)
                self.assertEqual(self.run_check(), 1)

    def test_name_that_git_quotes_fails(self):
        self.add("Schöger.pdf")
        self.assertEqual(self.run_check(), 1)

    def test_name_with_newline_fails(self):
        self.add("odd\nname.pdf")
        self.assertEqual(self.run_check(), 1)

    def test_other_book_formats_fail(self):
        for name in ("Schwabish.epub", "book.mobi", "ru.zip", "x.djvu"):
            with self.subTest(name=name):
                self.git("rm", "-rq", "--cached", "--ignore-unmatch", ".")
                self.add(name)
                self.assertEqual(self.run_check(), 1)

    def test_renamed_pdf_fails_by_content(self):
        self.add("notes.dat", b"%PDF-1.7\nrest")
        self.assertEqual(self.run_check(), 1)

    def test_large_file_fails(self):
        self.add("big.txt", b"x" * (1024 * 1024 + 1))
        self.assertEqual(self.run_check(), 1)

    def test_symbolic_link_fails(self):
        os.symlink("/somewhere/books", self.root / "link")
        self.git("add", "link")
        self.assertEqual(self.run_check(), 1)

    def test_renamed_epub_and_archives_fail_by_content(self):
        import io, zipfile
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w") as archive:
            archive.writestr("mimetype", "application/epub+zip")
        for name, content in (("book.dat", buffer.getvalue()), ("g.dat", b"\x1f\x8b rest"),
                              ("s.dat", b"7z\xbc\xaf rest"), ("r.dat", b"Rar! rest")):
            with self.subTest(name=name):
                self.git("rm", "-rq", "--cached", "--ignore-unmatch", ".")
                self.add(name, content)
                self.assertEqual(self.run_check(), 1)

    def test_more_archive_endings_fail(self):
        for name in ("b.tgz", "c.bz2", "d.xz", "e.zst", "f.cbz", "g.fb2", "h.chm", "i.ps"):
            with self.subTest(name=name):
                self.git("rm", "-rq", "--cached", "--ignore-unmatch", ".")
                self.add(name)
                self.assertEqual(self.run_check(), 1)

    def test_pdf_header_after_other_bytes_fails(self):
        self.add("late.dat", b"\n\n%PDF-1.7\nrest")
        self.assertEqual(self.run_check(), 1)

    def test_renamed_pdf_in_history_fails(self):
        self.add("d/x.bin", b"%PDF-1.7\nrest")
        self.git("commit", "-qm", "add")
        self.git("rm", "-q", "d/x.bin")
        self.git("commit", "-qm", "remove")
        self.assertEqual(self.run_check(), 0)
        self.assertEqual(self.run_check("--history"), 1)

    def test_clean_history_passes(self):
        self.add("README.md")
        self.git("commit", "-qm", "add")
        self.assertEqual(self.run_check("--history"), 0)

    def test_empty_repository_passes_history(self):
        self.assertEqual(self.run_check("--history"), 0)

    def test_submodule_fails_with_a_reason(self):
        self.add("README.md")
        self.git("commit", "-qm", "add")
        sha = subprocess.run(["git", "-C", str(self.root), "rev-parse", "HEAD"], capture_output=True,
                             text=True, check=True).stdout.strip()
        self.git("update-index", "--add", "--cacheinfo", f"160000,{sha},sm")
        result = subprocess.run([sys.executable, "-I", str(SCRIPT)], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("submodule", result.stderr)

    def test_git_failure_fails(self):
        with tempfile.TemporaryDirectory() as outside:
            self.assertEqual(self.run_check(cwd=outside), 2)

    def test_deleted_book_fails_in_history(self):
        self.add("a.pdf")
        self.git("commit", "-qm", "add")
        self.git("rm", "-q", "a.pdf")
        self.git("commit", "-qm", "remove")
        self.assertEqual(self.run_check(), 0)
        self.assertEqual(self.run_check("--history"), 1)


if __name__ == "__main__":
    unittest.main()
