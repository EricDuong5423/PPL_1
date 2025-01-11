"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/Shiba.Vo.Tien
 * Link Group : https://www.facebook.com/groups/khmt.ktmt.cse.bku
 * Date: 02.01.2025
"""
import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
#1. Mô tả chuỗi có độ dài lẻ
#     def test_001(self):
#         """test """
#         self.assertTrue(TestLexer.test("aaa*%","aaa*%,<EOF>",101))
#     def test_002(self):
#         """test """
#         self.assertTrue(TestLexer.test("ba aa","ba aa,<EOF>",102))
#     def test_003(self):
#         """test """
#         self.assertTrue(TestLexer.test("ba","Error Token ba",103))
#     def test_004(self):
#         """test """
#         self.assertTrue(TestLexer.test("","Error Token ",104))
#     def test_005(self):
#         """test """
#         self.assertTrue(TestLexer.test("a","a,<EOF>",105))

        
#2. Mô tả số thực trong C++.

    # def test_001(self):
    #     """test valid floating-point number"""
    #     self.assertTrue(TestLexer.test("3.14", "3.14,<EOF>", 101))

    # def test_002(self):
    #     """test valid floating-point number with no leading digit"""
    #     self.assertTrue(TestLexer.test(".5", ".5,<EOF>", 102))

    # def test_003(self):
    #     """test valid floating-point number in scientific notation"""
    #     self.assertTrue(TestLexer.test("1.23e-4", "1.23e-4,<EOF>", 103))

    # def test_004(self):
    #     """test valid floating-point number with positive exponent"""
    #     self.assertTrue(TestLexer.test("4.56E+10", "4.56E+10,<EOF>", 104))

    # def test_005(self):
    #     """test invalid floating-point number with missing exponent"""
    #     self.assertTrue(TestLexer.test("3.14e", "Error Token 3.14e", 105))

    # def test_006(self):
    #     """test invalid floating-point number with multiple dots"""
    #     self.assertTrue(TestLexer.test("3.14.5", "Error Token 3.14.5", 106))

    # def test_007(self):
    #     """test valid floating-point number with negative sign"""
    #     self.assertTrue(TestLexer.test("-3.14", "-3.14,<EOF>", 107))

    # def test_009(self):
    #     """test invalid floating-point number with letters"""
    #     self.assertTrue(TestLexer.test("3.14abc", "Error Token 3.14abc", 109))

    # def test_010(self):
    #     """test floating-point number with no fractional part"""
    #     self.assertTrue(TestLexer.test("5.", "5.,<EOF>", 110))

    # def test_011(self):
    #     """test valid scientific notation without fractional part"""
    #     self.assertTrue(TestLexer.test("1e10", "1e10,<EOF>", 111))

    # def test_012(self):
    #     """test invalid number starting with dot"""
    #     self.assertTrue(TestLexer.test(".e5", "Error Token .e5", 112))

    # def test_013(self):
    #     """test valid long double literal"""
    #     self.assertTrue(TestLexer.test("1.23l", "1.23l,<EOF>", 113))

    # def test_014(self):
    #     """test invalid exponent without base"""
    #     self.assertTrue(TestLexer.test("e5", "Error Token e5", 114))

    # def test_015(self):
    #     """test valid negative floating-point number in scientific notation"""
    #     self.assertTrue(TestLexer.test("-7.89e+2", "-7.89e+2,<EOF>", 115))

# 3. Mô tả chuỗi có nhiều nhất 4 chữ 'a'

    # def test_001(self):
    #     """Test chuỗi có 3 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaa", "aaa,<EOF>", 101))
    
    # def test_002(self):
    #     """Test chuỗi có 1 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("a", "a,<EOF>", 102))
    
    # def test_003(self):
    #     """Test chuỗi có 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaa", "aaaa,<EOF>", 103))
    
    # def test_004(self):
    #     """Test chuỗi không chứa chữ 'a'"""
    #     self.assertTrue(TestLexer.test("bcdef", "bcdef,<EOF>", 104))
    
    # def test_005(self):
    #     """Test chuỗi có 5 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aaaaa", "Error Token aaaaa", 105))
    
    # def test_006(self):
    #     """Test chuỗi có nhiều ký tự khác nhau nhưng không quá 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("abca", "abca,<EOF>", 106))
    
    # def test_007(self):
    #     """Test chuỗi có 0 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("bc", "bc,<EOF>", 107))
    
    # def test_008(self):
    #     """Test chuỗi có chữ 'a' nhưng không vượt quá số lần quy định"""
    #     self.assertTrue(TestLexer.test("a b c a", "a b c a,<EOF>", 108))
    
    # def test_009(self):
    #     """Test chuỗi có 5 chữ 'a' nhưng đã bị từ chối"""
    #     self.assertTrue(TestLexer.test("aaaaab", "Error Token aaaaab", 109))

# 4. Mô tả chuỗi có ít nhất 4 chữ 'a'

    # def test_001(self):
    #     """Test chuỗi có ít nhất 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaxaa", "aaxaa,<EOF>", 101))
    
    # def test_002(self):
    #     """Test chuỗi có đúng 4 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaab", "aaaab,<EOF>", 102))
    
    # def test_003(self):
    #     """Test chuỗi có 5 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaaa", "aaaaa,<EOF>", 103))
    
    # def test_004(self):
    #     """Test chuỗi có 6 chữ 'a'"""
    #     self.assertTrue(TestLexer.test("aaaaaa", "aaaaaa,<EOF>", 104))
    
    # def test_005(self):
    #     """Test chuỗi có ít hơn 4 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aa", "Error Token aa", 105))
    
    # def test_006(self):
    #     """Test chuỗi có 3 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("aaa", "Error Token aaa", 106))
    
    # def test_007(self):
    #     """Test chuỗi có ít hơn 4 chữ 'a' (lỗi)"""
    #     self.assertTrue(TestLexer.test("a b c", "Error Token a b c", 107))

# 5. Mô tả chuỗi mà a và b không kề nhau

    # def test_001(self):
    #     """Test chuỗi không có 'a' và 'b' kề nhau"""
    #     self.assertTrue(TestLexer.test("a", "a,<EOF>", 101))

    # def test_002(self):
    #     """Test chuỗi có 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("acb", "acb,<EOF>", 102))

    # def test_003(self):
    #     """Test chuỗi có nhiều ký tự khác, 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("axbxaxbxaxb", "axbxaxbxaxb,<EOF>", 103))

    # def test_004(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("ab", "Error Token ab", 104))

    # def test_005(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("ba", "Error Token ba", 105))

    # def test_006(self):
    #     """Test chuỗi có 'a' và 'b' kề nhau (lỗi)"""
    #     self.assertTrue(TestLexer.test("aabb", "Error Token aabb", 106))

    # def test_007(self):
    #     """Test chuỗi với ký tự không phải 'a' và 'b'"""
    #     self.assertTrue(TestLexer.test("123456", "123456,<EOF>", 107))

    # def test_008(self):
    #     """Test chuỗi có khoảng trắng giữa các ký tự"""
    #     self.assertTrue(TestLexer.test("a b c", "a b c,<EOF>", 108))

    # def test_009(self):
    #     """Test chuỗi có 'a' và 'b' không kề nhau"""
    #     self.assertTrue(TestLexer.test("a b", "a b,<EOF>", 109))
# 6. Mô tả chuỗi mà ký tự a phải nằm giữa 2 ký tự b, giữa a và b không có kí tự nào khác.
    # def test_001(self):
    #     """Test 'a' nằm giữa hai 'b'"""
    #     self.assertTrue(TestLexer.test("bab", "bab,<EOF>", 101))
    # def test_002(self):
    #     """Test chuỗi hợp lệ có nhiều lần 'bab'"""
    #     self.assertTrue(TestLexer.test("babbab", "babbab,<EOF>", 102))
    # def test_003(self):
    #     """Test chuỗi không hợp lệ với 'a' không nằm giữa 'b'"""
    #     self.assertTrue(TestLexer.test("ab", "Error Token ab", 103))
    # def test_004(self):
    #     """Test chuỗi có ký tự khác"""
    #     self.assertTrue(TestLexer.test("babc", "babc,<EOF>", 104))
    # def test_005(self):
    #     """Test chuỗi chỉ chứa 'a'"""
    #     self.assertTrue(TestLexer.test("a", "Error Token a", 105))
    # def test_006(self):
    #     """Test chuỗi chỉ chứa 'b'"""
    #     self.assertTrue(TestLexer.test("b", "Error Token b", 106))
    # def test_007(self):
    #     """Test chuỗi chứa 'baab'"""
    #     self.assertTrue(TestLexer.test("baab", "Error Token baab", 107))
    # def test_008(self):
    #     """Test chuỗi chứa 'baab'"""
    #     self.assertTrue(TestLexer.test("bbaabb", "Error Token bbaabb", 108))
    # def test_009(self):
    #     """Test chuỗi chứa dấu cách giữa 'b' và 'a'"""
    #     self.assertTrue(TestLexer.test("b a b", "Error Token b a b", 109))
# 7. Mô tả chuỗi a và b nằm xen kẽ nhau, ở giữa 2 a là 1 b, giữa 2 b là 1 a, giữa a và b có thể có những kí tự khác.
    # def test_001(self):
    #     """Test 'a' và 'b' xen kẽ với ký tự khác"""
    #     self.assertTrue(TestLexer.test("a#b", "a#b,<EOF>", 101))
    # def test_002(self):
    #     """Test nhiều lần 'a' và 'b' xen kẽ"""
    #     self.assertTrue(TestLexer.test("a#b@a$b", "a#b@a$b,<EOF>", 102))
    # def test_003(self):
    #     """Test hai 'a' liên tiếp"""
    #     self.assertTrue(TestLexer.test("aa", "Error Token aa", 103))
    # def test_004(self):
    #     """Test hai 'b' liên tiếp"""
    #     self.assertTrue(TestLexer.test("bb", "Error Token bb", 104))
    # def test_005(self):
    #     """Test chuỗi không xen kẽ"""
    #     self.assertTrue(TestLexer.test("abba", "Error Token abba", 105))
# 8. Mô tả chuỗi địa chỉ IPv4(A.B.C.D, với A,B,C,D trong đoạn [0;255].)
    # def test_001(self):
    #     """Test địa chỉ hợp lệ: Địa chỉ IPv4 cơ bản"""
    #     self.assertTrue(TestLexer.test("192.168.1.1", "192.168.1.1,<EOF>", 101))

    # def test_002(self):
    #     """Test địa chỉ hợp lệ: Các số nằm trong giới hạn"""
    #     self.assertTrue(TestLexer.test("255.255.255.255", "255.255.255.255,<EOF>", 102))

    # def test_003(self):
    #     """Test địa chỉ hợp lệ: Địa chỉ với số 0"""
    #     self.assertTrue(TestLexer.test("0.0.0.0", "0.0.0.0,<EOF>", 103))

    # def test_004(self):
    #     """Test địa chỉ hợp lệ: Địa chỉ với số một chữ số"""
    #     self.assertTrue(TestLexer.test("1.1.1.1", "1.1.1.1,<EOF>", 104))

    # def test_005(self):
    #     """Test địa chỉ hợp lệ: Địa chỉ hỗn hợp chữ số"""
    #     self.assertTrue(TestLexer.test("192.0.2.146", "192.0.2.146,<EOF>", 105))
    # def test_006(self):
    #     """Test không hợp lệ: Một phần vượt quá 255"""
    #     self.assertTrue(TestLexer.test("256.100.50.25", "Error Token 256.100.50.25", 106))

    # def test_007(self):
    #     """Test không hợp lệ: Thiếu một phần"""
    #     self.assertTrue(TestLexer.test("192.168.1", "Error Token 192.168.1", 107))

    # def test_008(self):
    #     """Test không hợp lệ: Có ký tự chữ trong địa chỉ"""
    #     self.assertTrue(TestLexer.test("192.abc.1.1", "Error Token 192.abc.1.1", 108))

    # def test_009(self):
    #     """Test không hợp lệ: Thiếu dấu chấm"""
    #     self.assertTrue(TestLexer.test("192168.1.1", "Error Token 192168.1.1", 109))

    # def test_010(self):
    #     """Test không hợp lệ: Có ký tự đặc biệt"""
    #     self.assertTrue(TestLexer.test("192.168@1.1", "Error Token 192.168@1.1", 110))

    # def test_011(self):
    #     """Test không hợp lệ: Thừa dấu chấm"""
    #     self.assertTrue(TestLexer.test("192.168..1.1", "Error Token 192.168..1.1", 111))
# 9. Mô tả mã màu hexa(VD: #FFFFFF).
    # def test_001(self):
    #     """Test mã màu hợp lệ: Tất cả chữ số"""
    #     self.assertTrue(TestLexer.test("#123456", "#123456,<EOF>", 801))

    # def test_002(self):
    #     """Test mã màu hợp lệ: Tất cả chữ cái hoa"""
    #     self.assertTrue(TestLexer.test("#ABCDEF", "#ABCDEF,<EOF>", 802))

    # def test_003(self):
    #     """Test mã màu hợp lệ: Tất cả chữ cái thường"""
    #     self.assertTrue(TestLexer.test("#abcdef", "#abcdef,<EOF>", 803))

    # def test_004(self):
    #     """Test mã màu hợp lệ: Kết hợp số và chữ cái"""
    #     self.assertTrue(TestLexer.test("#1a2B3c", "#1a2B3c,<EOF>", 804))
    # def test_005(self):
    #     """Test không hợp lệ: Thiếu dấu #"""
    #     self.assertTrue(TestLexer.test("123456", "Error Token 123456", 805))

    # def test_006(self):
    #     """Test không hợp lệ: Thiếu ký tự"""
    #     self.assertTrue(TestLexer.test("#12345", "Error Token #12345", 806))

    # def test_007(self):
    #     """Test không hợp lệ: Dư ký tự"""
    #     self.assertTrue(TestLexer.test("#1234567", "Error Token #1234567", 807))

    # def test_008(self):
    #     """Test không hợp lệ: Ký tự không hợp lệ"""
    #     self.assertTrue(TestLexer.test("#12G45H", "Error Token #12G45H", 808))

    # def test_009(self):
    #     """Test không hợp lệ: Ký tự đặc biệt"""
    #     self.assertTrue(TestLexer.test("#12@34$", "Error Token #12@34$", 809))

    # def test_010(self):
    #     """Test không hợp lệ: Trống"""
    #     self.assertTrue(TestLexer.test("", "Error Token ", 810))
# 10. Mô tả số hệ 8 trong C++.
    # def test_001(self):
    #     """Test số hệ 8 hợp lệ: Số đơn giản"""
    #     self.assertTrue(TestLexer.test("01234567", "01234567,<EOF>", 901))

    # def test_002(self):
    #     """Test số hệ 8 hợp lệ: Số 0"""
    #     self.assertTrue(TestLexer.test("0", "0,<EOF>", 902))

    # def test_003(self):
    #     """Test số hệ 8 hợp lệ: Số lẻ với nhiều chữ số"""
    #     self.assertTrue(TestLexer.test("07543210", "07543210,<EOF>", 903))

    # def test_004(self):
    #     """Test số hệ 8 hợp lệ: Số nhỏ nhất có hai chữ số"""
    #     self.assertTrue(TestLexer.test("01", "01,<EOF>", 904))
    # def test_005(self):
    #     """Test không hợp lệ: Chứa chữ số ngoài hệ 8"""
    #     self.assertTrue(TestLexer.test("089", "Error Token 089", 905))

    # def test_006(self):
    #     """Test không hợp lệ: Chứa ký tự chữ"""
    #     self.assertTrue(TestLexer.test("01a2345", "Error Token 01a2345", 906))

    # def test_007(self):
    #     """Test không hợp lệ: Chứa ký tự đặc biệt"""
    #     self.assertTrue(TestLexer.test("01@2345", "Error Token 01@2345", 907))

    # def test_008(self):
    #     """Test không hợp lệ: Số hệ 8 trống"""
    #     self.assertTrue(TestLexer.test("", "Error Token ", 908))
# 11. Mô tả số tự nhiên gồm 1 2 3, sao cho 2 chữ số liên tiếp không cách nhau 1 đơn vị
    # def test_001(self):
    #     """Test số tự nhiên hợp lệ: Không có chữ số liên tiếp cách nhau 1 đơn vị"""
    #     self.assertTrue(TestLexer.test("123", "Error Token 123", 1001))

    # def test_002(self):
    #     """Test số tự nhiên hợp lệ: Số chỉ có một chữ số"""
    #     self.assertTrue(TestLexer.test("1", "1,<EOF>", 1002))

    # def test_003(self):
    #     """Test số tự nhiên hợp lệ: Chuỗi chữ số ngẫu nhiên hợp lệ"""
    #     self.assertTrue(TestLexer.test("131", "131,<EOF>", 1003))

    # def test_004(self):
    #     """Test số tự nhiên không hợp lệ: Hai chữ số liên tiếp cách nhau 1 đơn vị"""
    #     self.assertTrue(TestLexer.test("12", "Error Token 12", 1004))

    # def test_005(self):
    #     """Test số tự nhiên không hợp lệ: Bắt đầu bằng một số hợp lệ nhưng vi phạm sau đó"""
    #     self.assertTrue(TestLexer.test("231", "Error Token 231", 1005))

    # def test_006(self):
    #     """Test số tự nhiên không hợp lệ: Toàn bộ chuỗi không hợp lệ"""
    #     self.assertTrue(TestLexer.test("121", "Error Token 121", 1006))

    # def test_007(self):
    #     """Test số tự nhiên không hợp lệ: Chuỗi trống"""
    #     self.assertTrue(TestLexer.test("", "Error Token ", 1007))

    # def test_008(self):
    #     """Test số tự nhiên hợp lệ: Dãy hợp lệ với độ dài lớn hơn"""
    #     self.assertTrue(TestLexer.test("313131", "313131,<EOF>", 1008))
# Mô tả một chuỗi tương tự thẻ div trong HTML, có thể có cả thẻ đóng - mở, hoặc chỉ có thẻ mở, nội dung giữa 2 thẻ là chuỗi bất kì, bên trong thẻ mở là các cặp attribute="value".
    def test_001(self):
        """Test thẻ div hợp lệ: Chứa thẻ mở và đóng, với các attribute hợp lệ"""
        self.assertTrue(TestLexer.test('<div class="container" id="main">Content here</div>', '<div class="container" id="main">Content here</div>,<EOF>', 1001))

    def test_002(self):
        """Test thẻ div hợp lệ: Chỉ có thẻ mở với các attribute hợp lệ"""
        self.assertTrue(TestLexer.test('<div class="header" style="color: red">Header content', '<div class="header" style="color: red">Header content,<EOF>', 1002))

    def test_003(self):
        """Test thẻ div hợp lệ: Thẻ mở và đóng, với attribute và nội dung tùy ý"""
        self.assertTrue(TestLexer.test('<div id="footer">Footer content</div>', '<div id="footer">Footer content</div>,<EOF>', 1003))

    def test_004(self):
        """Test thẻ div không hợp lệ: Sai cú pháp attribute trong thẻ mở"""
        self.assertTrue(TestLexer.test('<div class="container" style="color:red" >Content</div>', 'Error Token <div class="container" style="color:red" >Content</div>', 1004))

    def test_005(self):
        """Test thẻ div không hợp lệ: Cặp dấu ngoặc nhọn không tương ứng"""
        self.assertTrue(TestLexer.test('<div class="box">Content<div>', 'Error Token <div class="box">Content<div>', 1005))

    def test_006(self):
        """Test thẻ div không hợp lệ: Không có thẻ mở hay đóng"""
        self.assertTrue(TestLexer.test('', 'Error Token ', 1006))

    def test_007(self):
        """Test thẻ div không hợp lệ: Dài hơn với nhiều thẻ mở và đóng"""
        self.assertTrue(TestLexer.test('<div class="section"><div id="header">Header</div><div id="content">Content</div></div>', 'Error Token <div class="section"><div id="header">Header</div><div id="content">Content</div></div>,<EOF>', 1007))
