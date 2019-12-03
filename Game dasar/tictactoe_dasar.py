import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Pemain {row[0]} adalah pemenangnya karena sudah terpenuhi secara horizontal!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Pemain {check[0]} adalah pemenangnya karena sudah terpenuhi secara vertikal!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Pemain {diags[0]} adalah pemenangnya karena sudah terpenuhi secara Diagonal (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Pemain {diags[0]} adalah pemenangnya karena sudah terpenuhi secara Diagonal (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
            print("Ruang ini sudah terisi, silahkan coba yang lain!")
            return False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Apakah kamu bermain di kolom atau baris diluar batas diantara 0,1 atau 2? (IndexError)")
        return False
    except Exception as e:
        print(str(e))
        return False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"Pemain: {current_player}")
            column_choice = int(input("Kolom mana? "))
            row_choice = int(input("Baris mana? "))
            played = game_board(game, player=current_player, row=row_choice, column=column_choice)

        if win(game):
            game_won = True
            again = input("Game selesai, apakah anda ingin bermain lagi? (y/n) ")
            if again.lower() == "y":
                print("Memulai lagiiiii.....!")
            elif again.lower() == "n":
                print("Hey! \n sampai jumpa di lain hari \n untuk kita bertemu lagi...........")
                play = False
            else:
                print("Bukan jawaban yang benar, tapi.... sampai bertemu dilain kesempatan yaaaaa.........")
                play = False