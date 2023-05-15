"""Page info module"""
from dataclasses import dataclass

@dataclass
class PageInfo:
    """Page info"""
    title: str
    teaser: str
    non_full_text: str
    full_text: str

    def as_markdown(self):
        """Return page info as markdown"""
        text = f"# {self.title}\n"
        if self.teaser:
            text += f"## {self.teaser}\n"
        text += "\n"
        if self.non_full_text:
            text += f"{self.non_full_text}\n"

        if self.full_text:
            full_text = self.full_text.splitlines()
            full_text = '\n'.join([line for line in full_text if line])
            text += f"{full_text}\n"

        return text