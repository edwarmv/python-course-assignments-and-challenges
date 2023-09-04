from PIL import Image

mask = Image.open("./mask.png")

print("mask size:")
print(mask.size)  # 505 x 251

resized_mask = mask.resize((1015, 559))
resized_mask.putalpha(128)

word_matrix = Image.open("./word_matrix.png")


print("word_matrix size:")
print(word_matrix.size)  # 1015 x 559

word_matrix.paste(im=resized_mask, box=(0, 0), mask=resized_mask)
word_matrix.show()
