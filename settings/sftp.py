from django.conf import settings

from storages.backends.sftpstorage import SFTPStorage, SFTPStorageFile as SFTPBaseStorageFile

import posixpath
import lazy_object_proxy


class SFTPStorageStatic(SFTPStorage):

    def __init__(self, *args, **kwargs):
        super(SFTPStorageStatic, self).__init__(*args, **kwargs)
        self._base_url = settings.STATIC_URL
        self._root_path = settings.SFTP_STORAGE_ROOT + settings.STATIC_ROOT


class SFTPStorageFile(SFTPBaseStorageFile):

    def write(self, content):
        if 'w' not in self.mode:
            raise AttributeError("File was opened for read-only access.")
        self.file.write(content)
        self._is_dirty = True
        self._is_read = True


class SFTPStorageMedia(SFTPStorage):

    def __init__(self, *args, **kwargs):
        super(SFTPStorageMedia, self).__init__(*args, **kwargs)
        self._base_url = settings.MEDIA_URL
        self._root_path = settings.SFTP_STORAGE_ROOT + settings.MEDIA_ROOT

    def open(self, name, *args, **kwargs):
        ff = super(SFTPStorageMedia, self).open(name, *args, **kwargs)
        ff.name = name
        return ff

    def _open(self, name, mode='rb'):
        return SFTPStorageFile(name, self, mode)

    def _save(self, name, content):
        """Save file via SFTP."""
        path = self._remote_path(name)
        dirname = posixpath.dirname(path)
        if not self.exists(dirname):
            self._mkdir(dirname)

        if hasattr(content, 'open'):
            content.open()
            if isinstance(content, SFTPStorageFile):
                f_data = content.read()
            else:
                f_data = content.file.read()
        else:
            f_data = content

        f = self.sftp.open(path, 'wb')
        f.write(f_data)
        f.close()

        # set file permissions if configured
        if self._file_mode is not None:
            self.sftp.chmod(path, self._file_mode)
        if self._uid or self._gid:
            self._chown(path, uid=self._uid, gid=self._gid)
        return name


class SFTPFileManagerStorageMedia(SFTPStorageMedia):

    def __init__(self, *args, **kwargs):
        super(SFTPFileManagerStorageMedia, self).__init__(*args, **kwargs)
        self._base_url = settings.FILE_MANAGER_MEDIA_URL
        self._root_path = settings.SFTP_STORAGE_ROOT + settings.FILE_MANAGER_MEDIA_ROOT

LazySFTPFileManagerStorageMedia = lazy_object_proxy.Proxy(SFTPFileManagerStorageMedia)
