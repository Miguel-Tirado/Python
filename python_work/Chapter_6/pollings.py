fav_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

friends = ['phil','josh', 'david','becca','sarah','matt','danielle']
for friend in friends:
    if friend not in fav_languages.keys():
        print(f"{friend}, please take the poll.")
    else:
        print(f"{friend}, Thank you for taking the poll.")