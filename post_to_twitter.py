import pytz
import tweepy
import config
from datetime import datetime
from itertools import islice

def run():
    # use values set as variables on gitlab project
    client = tweepy.Client(
        consumer_key= config.consumer_key,
        consumer_secret = config.consumer_secret_key,
        access_token = config.access_token,
        access_token_secret = config.access_token_secret
    )

    # read details of the file containing today's extract
    with open('scratchier.txt', 'r') as file:
        file.seek(0)
        total_characters = len(file.read())  # count total characters
        file.seek(0)
        total_lines = len(file.readlines())  # count total lines

    tweet_text = ''
    header = str('\U0001F4C5 Updated ' + datetime.now(pytz.utc).strftime('%d %b %Y') + ' (' + datetime.now(pytz.utc).strftime('%Y/%m/%d')+ ')\n')

    # if there are less than x characters
    likely_empty_limit = 10
    character_limit = 240
    if total_characters < likely_empty_limit:
        tweet_text = header + 'The operations plan does not currently include any advisories for space operations.'
        tweet = client.create_tweet(text=tweet_text)
        print(tweet)
        #print(tweet_text)

    elif likely_empty_limit <= total_characters <= character_limit:
        with open('scratchier.txt', 'r') as file:
            tweet_text = header + file.read()
            tweet = client.create_tweet(text=tweet_text)
            print(tweet)
            #print(tweet_text)

    elif total_characters > character_limit:
        with open('scratchier.txt', 'r') as file:
            read_total_lines = file.readlines()
            max_lines = len(read_total_lines) # find how many lines the section of interest takes up
            blank_lines_array = [0] # create an array with the first line
            # append blank lines to array
            l_no = 0
            for x in read_total_lines:
                if x.strip() == '':
                    blank_lines_array.append(int(l_no))
                l_no += 1
            # append the last line to array
            blank_lines_array.append(int(max_lines))

            # find number of sections
            current_section = 1
            number_of_sections = len(blank_lines_array) - 1
            s = 0
            e = 1

            # for each section, repeat until max sections
            while current_section <= number_of_sections:
                file.seek(0)
                section = islice(file, blank_lines_array[s], blank_lines_array[e]) # extract this section
                # write section to buffer
                buffer = ''
                for x in section:
                    buffer = buffer + str(x)
                # set what to tweet depending on number of line breaks
                if str(buffer).startswith('\n'):
                    tweet_text = header + buffer
                    # tweet!
                    tweet = client.create_tweet(text=tweet_text)
                    print(tweet)
                else:
                    tweet_text = header + '\n' + buffer
                    # tweet!
                    tweet = client.create_tweet(text=tweet_text)
                    print(tweet)
                #print(tweet_text)
                # increase array start value, array end value, and session number by 1
                s += 1
                e += 1
                current_section += 1
