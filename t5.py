a = '<pclass="spoiler-tip">这篇影评可能有剧透</p>愈想愈气啊。来数数神奇动物在哪里3的几宗罪。1.严重文不'
#a.replace('<pclass="spoiler-tip">这篇影评可能有剧透</p>',"")
#head, sep, tail = str.partition('/')
a = a.split('</p>')
print(a[-1])
#print(a)