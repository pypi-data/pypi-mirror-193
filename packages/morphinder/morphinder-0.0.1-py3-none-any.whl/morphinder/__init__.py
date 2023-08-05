"""Top-level package for morphinder."""
import logging

log = logging.getLogger(__name__)

__author__ = "Florian Matter"
__email__ = "fmatter@mailbox.org"
__version__ = "0.0.1"


class Morphinder:
    def __init__(self, lexicon):
        self.cache = {}
        self.failed_cache = set()
        self.lexicon = lexicon

    def retrieve_morph_id(
        self,
        obj,
        gloss,
        morph_type,
        sense_key=None,
        id_key="ID",
        type_key="Type",
        gloss_key="Gloss",
        form_key="Form",
    ):
        if (obj, gloss) in self.cache:
            return self.cache[(obj, gloss)]
        if (
            obj,
            gloss,
        ) in self.failed_cache:  # failing silently (except for the first try)
            return None, None
        bare_gloss = gloss.strip("=").strip("-")
        candidates = self.lexicon[
            (self.lexicon[form_key].apply(lambda x: obj == x))
            & (self.lexicon[gloss_key].apply(lambda x: bare_gloss in x))
        ]
        if len(candidates) == 1:
            if sense_key:
                morph_id, sense = (
                    candidates.iloc[0][id_key],
                    candidates.iloc[0][sense_key][
                        candidates.iloc[0][gloss_key].index(bare_gloss)
                    ],
                )
                self.cache[(obj, gloss)] = (morph_id, sense)
                return (morph_id, sense)
            else:
                return candidates.iloc[0][id_key], None
        if len(candidates) > 0:
            narrow_candidates = candidates[candidates[type_key] == morph_type]
            if len(narrow_candidates) == 1:
                if sense_key:
                    return (
                        narrow_candidates.iloc[0][id_key],
                        narrow_candidates.iloc[0][sense_key][
                            narrow_candidates.iloc[0][gloss_key].index(bare_gloss)
                        ],
                    )
                else:
                    return narrow_candidates.iloc[0][id_key]
            log.warning(
                f"Multiple lexicon entries for {obj} '{gloss}', using the first hit:"
            )
            print(morph_type)
            print(candidates)
            if sense_key:
                return (
                    candidates.iloc[0][id_key],
                    candidates.iloc[0][sense_key][
                        candidates.iloc[0][gloss_key].index(bare_gloss)
                    ],
                )
            else:
                return candidates.iloc[0][id_key], None
        log.warning(f"No hits for /{obj}/ '{gloss}' in lexicon!")
        self.failed_cache.add((obj, gloss))
        return None, None
