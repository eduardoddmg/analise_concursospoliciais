def prepare_file(path, final, cols):
   f = open(path)
   text = f.read()
   f.close()

   text = text.replace('\n', ' ').replace(', ', ',').replace(' / ', '\n').replace('\n ', '\n')
   text = cols+text

   f = open(final, 'w')
   f.write(text)