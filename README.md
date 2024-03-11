<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Student Registration Form</title>
</head>
<body>

<h2>Student Registration Form</h2>

<form action="submit.php" method="post">
  <label for="name">Name:</label><br>
  <input type="text" id="name" name="name" required><br><br>

  <label for="dob">Date of Birth:</label><br>
  <input type="date" id="dob" name="dob" required><br><br>

  <label for="gender">Gender:</label><br>
  <input type="radio" id="male" name="gender" value="male" required>
  <label for="male">Male</label>
  <input type="radio" id="female" name="gender" value="female" required>
  <label for="female">Female</label><br><br>

  <label for="address">Address:</label><br>
  <textarea id="address" name="address" required></textarea><br><br>

  <label for="telephone">Telephone:</label><br>
  <input type="tel" id="telephone" name="telephone" pattern="[+255]{1}-[0-9]{7}" required><br><br>
  <small>Format: +255 7169052</small><br><br>

  <label for="email">Email Address:</label><br>
  <input type="email" id="email" name="email" required><br><br>

  <label for="course">Course:</label><br>
  <select id="course" name="course" required>
    <option value="">Select a course</option>
    <option value="Computer Science">Computer Science</option>
    <option value="Engineering">Engineering</option>
    <option value="Mathematics">Mathematics</option>
    <!-- Add more options as needed -->
  </select><br><br>

  <input type="submit" value="Register">
  <input type="button" value="Cancel" onclick="window.location.href='index.html'">
</form>

</body>
</html>
