import praw

_linux = ['linux']
_bsd = ['freebsd', 'netbsd', 'openbsd', 'bsd']
_ms = ['windows', 'microsoft', 'window$', 'micro$oft']

def count(s1, s2):
    i = 0
    j = 0
    while s1.find(s2, i) != -1:
        j += 1
        i = s1.find(s2, i) + 1
    return j

def xcount(s, a):
    ret = 0
    for i in a:
        i = ' ' + i + ' '
        ret += count(s.lower(), i)
    return ret

def zcount(texts, a):
    k = 0
    for i in texts:
        k += xcount(i, a)
    return k

def counter(subreddits):
    posts = 0
    coms = 0
    linux = 0
    bsd = 0
    ms = 0
    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).top('all', limit=100):
            posts += 1
            data = [submission.title, submission.selftext]
            ms += zcount(data, _ms)
            linux += zcount(data, _linux)
            bsd += zcount(data, _bsd)
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                coms += 1
                ms += xcount(comment.body, _ms)
                linux += xcount(comment.body, _linux)
                bsd += xcount(comment.body, _bsd)
    return [['Posts', posts], ['Comments', coms], ['Linux', linux], ['BSD', bsd], ['Microsoft', ms]]

reddit = praw.Reddit('bot1')

for i in counter(['linux', 'linuxmasterrace']):
    print(i[0], '=', i[1])