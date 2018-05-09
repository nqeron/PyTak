import unittest
import TakMove
import Symmetry


class ParseMoveTest(unittest.TestCase):
    def testNull(self):
        self.assertEqual("",TakMove.parse_move(""))

    def testPlacement(self):
        self.assertEqual("a5", TakMove.parse_move("P a5"))

    def testPlacementCapstone(self):
        self.assertEqual("Cb4", TakMove.parse_move("P b4 C"))

    def testPlacementWall(self):
        self.assertEqual("Sd3", TakMove.parse_move("P d3 W"))

    def testMoveUp(self):
        self.assertEqual("2a3+11", TakMove.parse_move("M a3 a5 1 1"))

    def testMoveDown(self):
        self.assertEqual("3a3-21", TakMove.parse_move("M a3 a1 2 1"))

    def testMoveLeft(self):
        self.assertEqual("3b3<", TakMove.parse_move("M b3 a3 3"))

    def testMoveRight(self):
        self.assertEqual("5c2>122", TakMove.parse_move("M c2 e3 1 2 2"))


class SlideTest(unittest.TestCase):
    def testSlideUp(self):
        self.assertEqual(TakMove.Slide.UP,TakMove.Slide.get_slide_val("2a3+11")) #Slide.UP

    def testSlideRight(self):
        self.assertEqual(TakMove.Slide.RIGHT,TakMove.Slide.get_slide_val("5b2>122")) #Slide.RIGHT

    def testSlideDown(self):
        self.assertEqual(TakMove.Slide.DOWN,TakMove.Slide.get_slide_val("c4-")) #Slide.DOWN

    def testSlideLeft(self):
        self.assertEqual(TakMove.Slide.LEFT,TakMove.Slide.get_slide_val("3b2<")) #Slide.LEFT


class ManhattenDistTest(unittest.TestCase):
    def testMDistHorizontalLine(self):
        self.assertEqual(4,Symmetry.m_dist(4,0,0,0))

    def testMDistHorizontalLine(self):
        self.assertEqual(5,Symmetry.m_dist(0,0,0,5))

    def testMDSegment(self):
        self.assertEqual(2,Symmetry.m_dist(1,1,2,2))

    def testMDLSegment(self):
        self.assertEqual(3,Symmetry.m_dist(1,3,3,4))



if __name__ == "__main__":
    unittest.main()