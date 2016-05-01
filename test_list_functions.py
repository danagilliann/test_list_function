import student_file # change accordingly if desired

class TestClass:
    test_list = [5, 9, "9", -2, 1, 3, True, 3]
    test_max = [-9, -1, -5]

    def test_listlen(self):
        assert student_file.listlen(self.test_list) == len(self.test_list)
    
    def test_listmax(self):
        assert student_file.listmax(self.test_max) == max(self.test_max)
    
    def test_listcopy(self):
        assert student_file.listcopy(self.test_list) == self.test_list
    
    def test_listappend(self):
        result = student_file.listappend(self.test_list, "poo")
        self.test_list.append("poo")
        assert result == self.test_list

    def test_listinsert(self):
        result = student_file.listinsert(self.test_list, 4, True)
        self.test_list.insert(4, True)
        assert result == self.test_list

    def test_listremove(self):
        result = student_file.listremove(self.test_list, 9)
        self.test_list.remove(9)
        assert result == self.test_list

    def test_listreverse(self):
        result = student_file.listreverse(self.test_list)
        self.test_list.reverse()
        assert result == self.test_list

