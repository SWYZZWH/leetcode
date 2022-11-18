class Solution:

    # def similarRGB(self, color: str) -> str:
    #
    #     def parse_color(s: str) -> int:
    #         return int(s, 16)
    #
    #     def similarity(s1: str, s2: str) -> int:
    #         return - (parse_color(s1) - parse_color(s2)) ** 2
    #
    #     def similarity(s1: int, s2: int) -> int:
    #         return - (s1 - s2) ** 2
    #
    #     def int2color(i: int) -> str:
    #         return format(i, "02x")
    #
    #     def highest_simi(s1: str) -> str:
    #         start_with = int(s1[0], 16)
    #         cur_simi = similarity(parse_color(s1), start_with * 16 + start_with)
    #         cur_str = int2color(start_with * 16 + start_with)
    #         if start_with < 15 and similarity(parse_color(s1), (start_with + 1) * 16 + start_with + 1) > cur_simi:
    #             cur_simi = similarity(parse_color(s1), (start_with + 1) * 16 + start_with + 1)
    #             cur_str = int2color((start_with + 1) * 16 + start_with + 1)
    #         if start_with > 0 and similarity(parse_color(s1), (start_with - 1) * 16 + start_with - 1) > cur_simi:
    #             cur_simi = similarity(parse_color(s1), (start_with - 1) * 16 + start_with - 1)
    #             cur_str = int2color((start_with - 1) * 16 + start_with - 1)
    #         return cur_str
    #
    #     return "#" + highest_simi(color[1:3]) + highest_simi(color[3:5]) + highest_simi(color[5:7])

    def similarRGB(self, color):
        def geClosest(s):
            return min(['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff'],
                       key=lambda x: abs(int(s, 16) - int(x, 16)))

        res = [geClosest(color[i:i + 2]) for i in range(1, len(color), 2)]
        return '#' + ''.join(res)