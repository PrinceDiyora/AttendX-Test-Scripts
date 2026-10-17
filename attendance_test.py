import unittest


def mark_attendance(attendance_records, student_id):
    """Mark attendance if the student is not already recorded."""
    if not student_id:
        return "Student ID is required"

    if student_id in attendance_records:
        return "Attendance already marked"

    attendance_records.add(student_id)
    return "Attendance marked successfully"


class AttendanceTest(unittest.TestCase):

    def test_mark_attendance(self):
        records = set()
        result = mark_attendance(records, "STU101")
        self.assertEqual(result, "Attendance marked successfully")

    def test_duplicate_attendance(self):
        records = {"STU101"}
        result = mark_attendance(records, "STU101")
        self.assertEqual(result, "Attendance already marked")

    def test_empty_student_id(self):
        records = set()
        result = mark_attendance(records, "")
        self.assertEqual(result, "Student ID is required")


if __name__ == "__main__":
    unittest.main()
