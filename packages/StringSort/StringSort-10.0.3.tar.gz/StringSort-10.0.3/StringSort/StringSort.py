class StringSort:
    """Library that helps with string: sort them,
    delete sings that are not useful,
    and so on!
    """

    def __init__(self, string):
        self.string = string

    def delete(self, strToDelete, second_sign = None):
        if second_sign:
            newStr = ''
            for i in range(0, len(self.string)):
                if self.string[i] in strToDelete and i < len(self.string) - 1 and\
                        self.string[i + 1] == str(second_sign):
                    continue
                newStr += self.string[i]

            return newStr
        else:
            newStr = ''
            for char in self.string:
                if char in strToDelete:
                    continue
                newStr += char

            return newStr

    def delete_with_space(self, strToDelete):
        newStr = ''
        for char in self.string:
            if char in strToDelete:
                if self.string[0] == char:
                    newStr = newStr
                    continue
                else:
                    newStr = newStr + ' '
                    continue
            newStr += char

        return newStr


    def alphabetical_order(self):
        """string in alphabetical order"""

        list1 = []
        list1.extend(self.string)
        list1.sort()
        return ''.join(list1)

    def which_one_delete(self, sing, number):
        f"""this method delete {number}th {sing} of the string"""

        self.sign = sing
        self.number = number
        list1 = []
        list1.extend(str(self.string))

        num = 0

        for i in range(len(list1)):
            if list1[i] == str(self.sign):
                num += 1
                if list1.count(self.sign) >= self.number:
                    if num == int(self.number):
                        list1[i] = ''
                else:
                    raise SyntaxError(f"your string '{self.string}' don't have {self.number} of '{self.sign}'")

        return ''.join(list1)

    def which_one_delete_with_space(self, sing, number):
        """this method delete number sing of the string with space"""

        self.sign = sing
        self.number = number
        list1 = []
        list1.extend(str(self.string))

        num = 0

        for i in range(len(list1)):
            if list1[i] == str(self.sign):
                num += 1
                if list1.count(self.sign) >= self.number:
                    if num == int(self.number):
                        list1[i] = ' '
                else:
                    raise SyntaxError(f"your string '{self.string}' don't have {self.number} of '{self.sign}'")

        return ''.join(list1)

    def same_signs(self, search_string):
        """this method will find same sings"""

        list1 = []

        list2 = []

        list1.extend(self.string)

        list2.extend(search_string)

        list3 = []

        if len(list1) <= len(list2):
            for i in range(len(list2)):
                if list2[i] != ' ':
                    for j in list1:
                        if list2[i] == j:
                            list3.append(j)
                            list1.remove(j)
        else:
            raise SyntaxError(f"string '{list1}' is bigger than '{list2}'")

        return ', '.join(list3)

    def delete_all_types_of_parentheses(self):
        """method to delete all types of parentheses from string"""

        list1 = []
        list1.extend(str(self.string))

        if ('(' in list1) and (')' in list1) and ('{' in list1) and ('}' in list1) and ('[' in list1) and (']' in list1):
            for i in range(len(list1)):
                if (list1[i] == '(') | (list1[i] == '[') | (list1[i] == '{') | \
                        (list1[i] == '}') | (list1[i] == ']') | (list1[i] == ')'):
                    list1[i] = ''
            return ''.join(list1)
        else:
            raise SyntaxError(self.string + " don't have '{}', '[]' or '()'")

    def delete_all_types_of_parentheses_with_space(self):
        """method to delete all types of parentheses from string with space"""

        list1 = []
        list1.extend(str(self.string))

        if ('(' in list1) | (')' in list1) | ('{' in list1) | ('}' in list1) | ('[' in list1) | (']' in list1):
            for i in range(len(list1)):
                if (list1[i] == '(') | (list1[i] == '[') | (list1[i] == '{') | \
                        (list1[i] == '}') | (list1[i] == ']') | (list1[i] == ')'):
                    list1[i] = ' '
            return ''.join(list1)
        else:
            raise SyntaxError(self.string + " don't have '{}', '[]' or '()'")

    def split(self, number_of_signs):
        list1 = []
        list1.extend(self.string)

        num = 0

        for i in range(len(list1)):
            num += 1

            if num == number_of_signs:
                if i < len(list1) - 1:
                    if (list1[i + 1] == ' ') or (list1[i + 1] == '.') or (list1[i + 1] == ',') \
                            or (list1[i + 1] == '?') or (list1[i + 1] == '!'):
                        list1[i + 1] = list1[i + 1] + '\n'
                        num = 0
                    else:
                        list1[i] = list1[i] + '-' + '\n'
                        num = 0

        return ''.join(list1)

    def __repr__(self):
        return self.string