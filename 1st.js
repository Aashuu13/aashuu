<!DOCTYPE html>
<html>
<body>
<h1>JavaScript if</h1>

<p id="demo"></p>

<script>
let age = 16;
let text = "You can Not drive!";

if (age >= 18) {
  text = "You can drive!";
}

document.getElementById("demo").innerHTML = text;
</script>

</body>
</html>

