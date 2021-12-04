import statistics
from statistics import mode

# def most_common(List):
#     return(mode(List))

# List = [2, 1, 2, 2, 1, 3]
# print(most_common(List))

a = [(380, 429, 4, 5), (299, 429, 7, 6), (49, 429, 4, 6), (202, 428, 6, 7), (45, 427, 4, 4), (388, 425, 4, 9), (380, 424, 7, 5), (38, 424, 6, 11), (377, 424, 18, 11), (291, 424, 18, 12), (190, 424, 26, 11), (96, 424, 22, 14), (5, 424, 51, 11), (385, 369, 7, 6), (302, 365, 4, 9), (380, 364, 7, 6), (38, 364, 6, 11), (377, 364, 18, 12), (291, 364, 18, 11), (190, 364, 26, 11), (96, 364, 22, 14), (5, 364, 51, 11), (385, 309, 7, 6), (380, 309, 4, 5), (49, 309, 4, 6), (202, 308, 6, 7), (302, 305, 4, 9), (111, 305, 4, 9), (380, 304, 7, 6), (38, 304, 6, 11), (377, 304, 18, 11), (291, 304, 18, 11), (190, 304, 26, 11), (96, 304, 22, 14), (5, 304, 51, 11), (380, 249, 4, 5), (46, 249, 7, 6), (388, 245, 4, 9), (302, 245, 4, 9), (294, 245, 7, 5), (111, 245, 4, 9), (380, 244, 7, 5), (38, 244, 6, 11), (377, 244, 18, 11), (291, 244, 18, 11), (190, 244, 26, 11), (96, 244, 22, 14), (5, 244, 51, 12), (46, 18, 364, 18, 11), (190, 364, 26, 11), (96, 364, 22, 14), (5, 364, 51, 11), (385, 309, 7, 6), (380, 309, 4, 5), (49, 309, 4, 6), (202, 308, 6, 7), (302, 305, 4, 9), (111, 305, 4, 9), (380, 304, 7, 6), (38, 304, 6, 11), (377, 304, 18, 11), (291, 304, 18, 11), (190, 304, 26, 11), (96, 304, 22, 14), (5, 304, 51, 11), (380, 249, 4, 5), (46, 249, 7, 6), (388, 245, 4, 9), (302, 245, 4, 9), (294, 245, 7, 5), (111, 245, 4, 9),
     (380, 244, 7, 5), (38, 244, 6, 11), (377, 244, 18, 11), (291, 244, 18, 11), (190, 244, 26, 11), (96, 244, 22, 14), (5, 244, 51, 12), (46, 188, 7, 6), (38, 188, 6, 6), (202, 187, 6, 7), (392, 184, 4, 9), (384, 184, 4, 9), (302, 184, 4, 9), (41, 184, 6, 5), (49, 183, 4, 6), (374, 183, 25, 11), (291, 183, 18, 12), (190, 183, 26, 11), (96, 183, 22, 14), (5, 183, 51, 11), (49, 128, 4, 6), (38, 128, 6, 6), (388, 124, 4, 9), (302, 124, 4, 9), (380, 123, 4, 6), (41, 123, 7, 6), (377, 123, 18, 12), (291, 123, 18, 11), (190, 123, 26, 11), (96, 123, 22, 14), (5, 123, 51, 11), (192, 66, 22, 8), (348, 51, 4, 4), (386, 50, 4, 5), (365, 50, 6, 5), (306, 49, 4, 6), (356, 48, 4, 7), (288, 48, 4, 7), (267, 48, 9, 7), (187, 48, 8, 7), (169, 48, 6, 4), (114, 48, 4, 7), (107, 48, 6, 4), (102, 48, 4, 7), (381, 47, 4, 4), (297, 47, 7, 8), (180, 47, 6, 8), (164, 47, 4, 8), (96, 47, 5, 8), (403, 47, 21, 8), (161, 47, 83, 12), (91, 47, 32, 12), (315, 32, 4, 4), (126, 32, 4, 4), (118, 31, 7, 5), (85, 31, 7, 5), (20, 31, 4, 5), (382, 29, 4, 7), (297, 29, 4, 7), (224, 29, 4, 7), (208, 29, 6, 7), (320, 28, 6, 5), (315, 28, 4, 4), (306, 28, 4, 4), (126, 28, 4, 4), (175, 27, 4, 7), (170, 27, 4, 7), (372, 25, 4, 11), (20, 25, 4, 4), (367, 25, 38, 11), (167, 25, 72, 15), (65, 25, 84, 11), (16, 25, 28, 15), (269, 24, 61, 16)]
a.sort(key=lambda x: x[1], reverse=False)
print(a)