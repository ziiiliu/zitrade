from enum import Enum, auto

class OddsApiSports(Enum):
    NCAAF = auto()
    NFL = auto()
    NFLSUPER = auto()
    AFL = auto()
    ATPFRENCH = auto()
    WTAFRENCH = auto()

SPORTS_MAPPING = {
    OddsApiSports.NCAAF: "americanfootball_ncaaf",
    OddsApiSports.NFL: "americanfootball_nfl",
    OddsApiSports.NFLSUPER: "americanfootball_nfl_super_bowl_winner",
    OddsApiSports.AFL: "aussierules_afl",
    OddsApiSports.ATPFRENCH: "tennis_atp_french_open",
    OddsApiSports.WTAFRENCH: "tennis_wta_french_open",
}