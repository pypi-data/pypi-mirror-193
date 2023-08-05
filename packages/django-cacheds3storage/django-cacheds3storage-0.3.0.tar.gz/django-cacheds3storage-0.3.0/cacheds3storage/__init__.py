import os
from storages.backends.s3boto3 import S3Boto3Storage, SpooledTemporaryFile
from django.conf import settings
from dateutil import tz


class CachedS3BotoStorage(S3Boto3Storage):
    # https://github.com/jschneier/django-storages/issues/382
    #    #issuecomment-592876060
    def _save(self, name, content):
        """
        We create a clone of the content file as when this is passed
        to boto3 it wrongly closes the file upon upload where as the
        storage backend expects it to still be open
        """
        # Seek our content back to the start
        content.seek(0, os.SEEK_SET)

        # Create a temporary file that will write to disk after a
        # specified size. This file will be automatically deleted when
        # closed by boto3 or after exiting the `with` statement if the
        # boto3 is fixed
        with SpooledTemporaryFile() as content_autoclose:

            # Write our original content into our copy that will be
            # closed by boto3
            content_autoclose.write(content.read())

            # Upload the object which will auto close the
            # content_autoclose instance
            return super(CachedS3BotoStorage, self)._save(
                name, content_autoclose)

    def modified_time(self, prefixed_path):
        # S3Boto3Storage returns a UTC timestamp (which it gets from S3)
        # but an offset-naive one.
        # collectstatic needs to compare that timestamp against
        # a local timestamp (but again an offset-naive one)
        # so here, we need to convert our naive UTC to a naive local
        # takes a few steps...

        # get the offset-naive UTC timestamp
        r = super(CachedS3BotoStorage, self).modified_time(prefixed_path)

        # make it offset-aware
        from_zone = tz.gettz('UTC')
        to_zone = tz.gettz(settings.TIME_ZONE)
        utc = r.replace(tzinfo=from_zone)

        # convert it to a local offset-aware one
        lcl = utc.astimezone(to_zone)

        # then make it offset-naive
        naive = lcl.replace(tzinfo=None)
        return naive


class CompressorS3BotoStorage(CachedS3BotoStorage):
    location = 'media'


class MediaRootS3BotoStorage(CachedS3BotoStorage):
    location = 'uploads'
