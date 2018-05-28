import unittest
import TakMove
import Symmetry


class ParseMoveTest(unittest.TestCase):
    def testNull(self):
        self.assertEqual("", TakMove.parse_server_move(""))

    def testPlacement(self):
        self.assertEqual("a5", TakMove.parse_server_move("P a5"))

    def testPlacementCapstone(self):
        self.assertEqual("Cb4", TakMove.parse_server_move("P b4 C"))

    def testPlacementWall(self):
        self.assertEqual("Sd3", TakMove.parse_server_move("P d3 W"))

    def testMoveUp(self):
        self.assertEqual("2a3+11", TakMove.parse_server_move("M a3 a5 1 1"))

    def testMoveDown(self):
        self.assertEqual("3a3-21", TakMove.parse_server_move("M a3 a1 2 1"))

    def testMoveLeft(self):
        self.assertEqual("3b3<", TakMove.parse_server_move("M b3 a3 3"))

    def testMoveRight(self):
        self.assertEqual("5c2>122", TakMove.parse_server_move("M c2 e3 1 2 2"))


class SlideTest(unittest.TestCase):
    def testSlideUp(self):
        self.assertEqual(TakMove.Slide.UP,TakMove.Slide.get_slide_val("2a3+11")) #Slide.UP

    def testSlideRight(self):
        self.assertEqual(TakMove.Slide.RIGHT,TakMove.Slide.get_slide_val("5b2>122")) #Slide.RIGHT

    def testSlideDown(self):
        self.assertEqual(TakMove.Slide.DOWN,TakMove.Slide.get_slide_val("c4-")) #Slide.DOWN

    def testSlideLeft(self):
        self.assertEqual(TakMove.Slide.LEFT, TakMove.Slide.get_slide_val("3b2<")) #Slide.LEFT

    def testSlideStr(self):
        self.assertEqual("+", str(TakMove.Slide.UP))


class ManhattenDistTest(unittest.TestCase):
    def testMDistHorizontalLine(self):
        self.assertEqual(4, Symmetry.m_dist(4, 0, 0, 0))

    def testMDistHorizontalLine(self):
        self.assertEqual(5, Symmetry.m_dist(0, 0, 0, 5))

    def testMDSegment(self):
        self.assertEqual(2, Symmetry.m_dist(1, 1, 2, 2))

    def testMDLSegment(self):
        self.assertEqual(3, Symmetry.m_dist(1, 3, 3, 4))


class SymmetryTests(unittest.TestCase):
    def testGetSquare(self):
        self.assertEqual("b5", Symmetry.get_square("b5"))
        self.assertEqual("c3", Symmetry.get_square("c3+"))
        self.assertEqual("d4", Symmetry.get_square("5d4-"))
        self.assertEqual("a1", Symmetry.get_square("3a1+21"))
        self.assertEqual("e2", Symmetry.get_square("Ce2"))

    def testGetColumn(self):
        self.assertEqual(0, Symmetry.get_col_num("a3"))
        self.assertEqual(0, Symmetry.get_col_num("a2"))
        self.assertEqual(1, Symmetry.get_col_num("b4"))
        self.assertEqual(2, Symmetry.get_col_num("c1"))
        self.assertEqual(3, Symmetry.get_col_num("d5"))
        self.assertEqual(4, Symmetry.get_col_num("e2"))
        self.assertEqual(5, Symmetry.get_col_num("f6"))

    def testGetRow(self):
        self.assertEqual(2, Symmetry.get_row_num("a3"))
        self.assertEqual(1, Symmetry.get_row_num("a2"))
        self.assertEqual(3, Symmetry.get_row_num("b4"))
        self.assertEqual(0, Symmetry.get_row_num("c1"))
        self.assertEqual(5, Symmetry.get_row_num("d6"))
        self.assertEqual(1, Symmetry.get_row_num("e2"))
        self.assertEqual(4, Symmetry.get_row_num("f5"))

    def testXFlipFive(self):
        self.assertEqual(["5e4<", "4d2+31", "a1", "b3>", "3c5-111"],
                         Symmetry.mirror_x(["5a4>", "4b2+31", "e1", "d3<", "3c5-111"], 5))

    def testXFlipSix(self):
        self.assertEqual(["5e4<", "4d2+31", "a1", "b3>", "3c5-111", "Cf4"],
                         Symmetry.mirror_x(["5b4>", "4c2+31", "f1", "e3<", "3d5-111", "Ca4"], 6))

    def testYFlipFive(self):
        self.assertEqual(["5a1>", "4b2+31", "c3<", "3d4-111", "e5"],
                         Symmetry.mirror_y(["5a5>", "4b4-31", "c3<", "3d2+111", "e1"], 5))

    def testYFlipSix(self):
        self.assertEqual(["5a1>", "4b2+31", "c3<", "3d4-111", "e5", "Cf6"],
                         Symmetry.mirror_y(["5a6>", "4b5-31", "c4<", "3d3+111", "e2", "Cf1"], 6))

    def testDiagFlipFive(self):
        self.assertEqual(["5a1>", "4b3+31", "c4<", "3d5-111", "e2"],
                         Symmetry.mirror_diag(["5a1+", "4c2>31", "d3-", "3e4<111", "b5"], 5))

    def testDiagFlipSix(self):
        self.assertEqual(["5a1>", "4b3+31", "c4<", "3d6-111", "e2", "Cf5"],
                         Symmetry.mirror_diag(["5a1+", "4c2>31", "d3-", "3f4<111", "b5", "Ce6"], 6))


if __name__ == "__main__":
    unittest.main()
