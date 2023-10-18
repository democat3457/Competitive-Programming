"""
BEGIN ANNOTATION
PROBLEM URL: https://open.kattis.com/problems/lost
TAGS: graphs, bfs
EXPLANATION:
Construct a graph of languages connected via translations, then perform BFS starting from
the English node, as the problem emphasizes distance to the English node. In a separate
dictionary, store the found languages and their respective immediate translator cost. If,
in one iteration of BFS (same distance to English), multiple translators are found for a
particular language, take the minimum cost of all translators that satisfy that language.
After every iteration, filter the languages list to determine what languages still need to
be found. If, during an iteration, no translation connections are found, then we have
exhausted all available connections. If there are still remaining target languages, then
those are unreachable from the English node, so print "Impossible"; otherwise, we have
successfully translated all the languages, so we print the sum of the costs of all
immediate translators.
END ANNOTATION
"""

from collections import defaultdict

n,m = map(int, input().split())
languages = input().split()
translations = defaultdict(dict)
for _ in range(m):
    a,b,i = input().split()
    i = int(i)
    translations[a][b] = i
    translations[b][a] = i

for lang in languages:
    if lang not in translations:
        print('Impossible')
        quit()

found_languages = { "English" : 0 }

found = True
while found:
    found = False
    copy_found = found_languages.copy()
    for lang in languages:
        tr = translations[lang]
        for found_lang in copy_found:
            if found_lang in tr:
                f = found_languages[found_lang]
                if lang in found_languages:
                    found_languages[lang] = min(found_languages[lang], tr[found_lang])
                else:
                    found_languages[lang] = tr[found_lang]
                found = True
    languages = [ lang for lang in languages if lang not in found_languages ]

if len(languages):
    print('Impossible')
else:
    print(sum(found_languages.values()))
