import pandas as pd
import random

CIV_DATA_PATH = "leaders.csv"
# Put the players you want to draft in here
PLAYERS = [
    "Jasper",
    "Jason",
    "Connor",
    "Elliot",
    "Liz",
    "Jaspers_Other_Friend",
    "Anita",
    "Jeremiah"
]

def partition_dataset(civ_df, num_rows_to_sample, with_replacement=False):
    """Returns sampled_df (with `num_rows_to_sample` rows), and
    remaining_df (with the rest)

    Args:
        civ_df: pandas DataFrame from parsed Civ Data (`leaders.csv`)
        num_rows_to_sample: Number of rows to sample rom each data set
        with_replacement: Whether or not to sample with replacement

    Returns:
        (sampled_df, rest_df), in which:
          sampled_df: Civs drafted for one player (pandas DataFrame)
          rest_df: All Civs not yet drafted for one player (pandas DataFrame)
    """

    # Samples Civs picked for player
    sample_df = civ_df.sample(n=num_rows_to_sample)
    # Gets remaining Civs
    if with_replacement:
        rest_df = civ_df
    else:
        rest_df = civ_df.loc[~civ_df.index.isin(sample_df.index)]

    return (sample_df, rest_df)

def draft_civs(players=PLAYERS,options_per_player=4):
    """Drafts all players in `players`, with `options_per_player`
    civ options per player.

    Args:
        players: List<str> of the players you are drafting for
        options_per_player: How many Civ options should we give each player in
          our draft?
    """

    # These are string builder lists that will contain our draft output
    basic_draft_string_builder = [] # for everyone to see
    detailed_draft_string_builder = [] # for each specific player

    # Reads in our Civ DF, makes sure that the dataset is valid
    civ_df = pd.read_csv(CIV_DATA_PATH)
    civ_df["nice_short_output"] = civ_df["nation"] + " (" + civ_df["leader"] + ")"

    # (we should have only Eleanor of Aquitaine be repeated)
    seen_leaders = set()
    for _, row in civ_df.iterrows():
        if row['leader'] in seen_leaders:
            print(f"Repeated Leader:  {row['leader']}")
        seen_leaders.add(row['leader'])


    # Drafts each player in turn, only writing out the
    rest_df = civ_df
    player_draft_data_list = []
    for player in PLAYERS:
        # Drafts given player (without replacement)
        sample_df, rest_df = partition_dataset(civ_df=rest_df,
                                               num_rows_to_sample=options_per_player)

        # Writes basic player headers
        basic_draft_string_builder.append(f"-- {player} --")
        detailed_draft_string_builder.append(f">>> FOR {player.upper()}")

        # Writes Civ-by-Civ info
        index = 1
        for _, row in sample_df.iterrows():
            # Writes short draft info
            basic_draft_string_builder.append(f"{row['nice_short_output']}")

            # Writes detailed draft into
            detailed_draft_string_builder.append(f"Country {index}: {row['nation']} ({row['leader']})")
            detailed_draft_string_builder.append(f"-- Country Ability: '{row['ability_name']}'\n{row['ability_desc']}")
            detailed_draft_string_builder.append(f"-- Leader Ability: '{row['bonus_name']}''\n{row['bonus_desc']}'\n\n")
            index += 1

    # Outputs the draft strings to files
    basic_file = open("basic_draft.txt", "w")
    basic_file.write("\n".join(basic_draft_string_builder))

    detailed_file = open("detailed_draft.txt", "w")
    detailed_file.write("\n".join(detailed_draft_string_builder))



if __name__ == "__main__":
    draft_civs()
