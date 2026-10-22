from datetime import datetime

class VersionManager:
    VERSION="THIP_v0.3"

    def current_version(self)->str:
        return self.VERSION

    def timestamp(self)->str:
        return datetime.now().isoformat(timespec="seconds")
