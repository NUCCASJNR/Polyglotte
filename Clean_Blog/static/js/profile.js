const profilePic = document.getElementById("profile_pic");
const inputFile = document.getElementById("input_file");

inputFile.onchange = function () {
    profilePic.src = URL.createObjectURL(inputFile.files[0])
}