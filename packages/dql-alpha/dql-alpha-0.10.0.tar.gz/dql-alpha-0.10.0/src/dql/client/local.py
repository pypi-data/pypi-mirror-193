import posixpath
from datetime import datetime, timezone
from pathlib import Path
from typing import Tuple

from fsspec.implementations.local import LocalFileSystem

from .fsspec import FSSpecClient


class FileClient(FSSpecClient):
    FS_CLASS = LocalFileSystem
    PREFIX = "file://"
    protocol = "file"

    @classmethod
    def ls_buckets(cls, **kwargs):
        return []

    @classmethod
    def split_url(cls, url: str, data_storage) -> Tuple[str, str]:
        # pylint:disable=protected-access
        if data_storage.get_storage(url):
            return LocalFileSystem._strip_protocol(url), ""
        for pos in range(len(url) - 1, len(cls.PREFIX), -1):
            if url[pos] == "/" and data_storage.get_storage(url[:pos]):
                return LocalFileSystem._strip_protocol(url[:pos]), url[pos + 1 :]
        raise RuntimeError(f"Invalid file path '{url}'")

    async def ls_dir(self, path):
        return self.fs.ls(path, detail=True)

    def rel_path(self, path):
        return posixpath.relpath(path, self.name)

    @property
    def uri(self):
        return Path(self.name).as_uri()

    def get_full_path(self, rel_path):
        full_path = Path(self.name, rel_path).as_uri()
        if rel_path.endswith("/") or not rel_path:
            full_path += "/"
        return full_path

    def _dict_from_info(self, v, parent_id, delimiter, path):
        name = posixpath.basename(path)
        return {
            "dir_id": None,
            "parent_id": parent_id,
            "path": self.rel_path(v["name"]),
            "name": name,
            "checksum": "",
            "etag": "",
            "version": "",
            "is_latest": True,
            "last_modified": datetime.fromtimestamp(v["mtime"], timezone.utc),
            "size": v.get("size", ""),
            "owner_name": "",
            "owner_id": "",
            "anno": None,
        }
