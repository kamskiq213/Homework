a = open('story.txt','r').read().replace('python','java')
b = open('new_story.txt','w').write(a)