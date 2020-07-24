from google.cloud import datastore


class DSClient(datastore.Client):
    """A DataStrore client"""

    def list_kinds(self, users=True):
        """List kinds

        :type users: bool
        :param user: if only list user defined kind. default is True
        """
        query = self.query(kind="__kind__")
        kinds = [entity.key.id_or_name for entity in query.fetch()]
        if users:
            return [k for k in kinds if not k.startswith("_")]
        return kinds

    def get_keys(self, kind, limit=10):
        """Get a number of keys of a Kind"""
        q = self.query(kind=kind)
        q.keys_only()
        return [e.key.id_or_name for e in q.fetch(limit=limit)]
