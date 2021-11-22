#!/usr/bin/python3
# Hangman game

import logging
import mysql.connector
import random
import configparser
import time

# Sāk laika atskaiti kad tiek palaista programma
start_time = time.monotonic()

########
# Config.ini inicalizēšana
config = configparser.ConfigParser()
config.read('./config.ini')
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

# Žurnalizēšanas kommandrinda
logging.basicConfig(filename='hangman_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                    user=mysql_config_mysql_user, password=mysql_config_mysql_pass)

mycursor = connection.cursor()


"""
ant baboon badger bat bear beaver camel cat clam cobra cougar coyote
crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama
mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram
rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger
toad trout turkey turtle weasel whale wolf wombat zebra
"""







# kārātuves zīmējums
class HangMan(object):
    # Hangman game
    # hang variable visu apvieno kopā lai izveidotu karātuves
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')
    # man variable izveido cilvēciņu
    man = {}
    man[0] = [' 0   |']
    man[1] = [' 0   |', ' |   |']
    man[2] = [' 0   |', '/|   |']
    man[3] = [' 0   |', '/|\\  |']
    man[4] = [' 0   |', '/|\\  |', '/    |']
    man[5] = [' 0   |', '/|\\  |', '/ \\  |']

    pics = []
    # words variable ir vārdu kopums no kura paņem random vārdu un to izmanto priekš spēles
    words = '''ant cat'''.split()

    infStr = '_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''

    def __init__(self, *args, **kwargs):
        i, j = 2, 0
        self.pics.append(self.hang[:])
        for ls in self.man.values():
            pic, j = self.hang[:], 0
            for m in ls:
                pic[i + j] = m
                j += 1
            self.pics.append(pic)

    # izvēlas random vārdu
    def pickWord(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    def printPic(self, idx, wordLen):
        for line in self.pics[idx]:
            print(line)

    def askAndEvaluate(self, word, result, missed):
        guess = input()
        #
        logging.info('Player chose letter ' + guess)
        if guess == None or len(guess) != 1 or (guess in result) or (guess in missed):
            return None, False
        i = 0
        right = guess in word
        for c in word:
            if c == guess:
                result[i] = c
            i += 1
        return guess, right

    def info(self, info):
        ln = len(self.infStr)
        print(self.infStr[:-3])
        print(info)
        print(self.infStr[3:])

    def start(self):
        logging.info('***NEW GAME***')
        print('Welcome to Hangman !')
        word = list(self.pickWord())
        result = list('*' * len(word))
        print('The word is: ', result)
        success, i, missed = False, 0, []
        while i < len(self.pics) - 1:
            print('Guess the word: ', end='')
            guess, right = self.askAndEvaluate(word, result, missed)
            if guess == None:
                print('You\'ve already entered this character.')
                continue
            print(''.join(result))
            if result == word:
                vards = ''.join(word)
                logging.info('Player won! The word was he guessed was - ' + vards)
                time_win = time.monotonic() - start_time
                time_win = round(time_win, 2)
                print('seconds: ', time_win)

                mycursor.execute(
                    "INSERT INTO `min_vardi` (`vardi`, `atrums`,`status`) VALUES ('" + str(vards) + "','" + str(
                        time_win) + "','win' )")
                connection.commit()

                self.info('Congratulations ! You\'ve just saved a life !')
                success = True
                print(result)
                break
            if not right:
                missed.append(guess)
                i += 1
            self.printPic(i, len(word))
            print('Missed characters: ', missed)

        if not success:
            vards = ''.join(word)
            logging.info('Player lost, player had to guess the word - ' + vards)
            time_lose = time.monotonic() - start_time
            time_lose = round(time_lose, 2)
            mycursor.execute(
                "INSERT INTO `min_vardi` (`vardi`, `atrums`,`status`) VALUES ('" + str(vards) + "','" + str(time_lose) + "','lose')")

            connection.commit()


            self.info('The word was \'' + ''.join(word) + '\' ! You\'ve just killed a man, yo !')


a = HangMan().start()

mycursor.execute(
    "INSERT INTO `data` (`name`, `score`,`guesses`) VALUES ('" + str(name) + "','" + str(score) + "','" + str(number_of_guesses) + "'")

connection.commit()


