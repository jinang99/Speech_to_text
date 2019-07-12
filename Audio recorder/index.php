<!DOCTYPE html>
<?php
  $servername = "localhost:3307";
  $username = "root";
  $password = "";
  $dbname = "sai_estate";

  // Create connection
  $conn = new mysqli($servername, $username, $password, $dbname);
  // Check connection
  if ($conn->connect_error) 
  {
    die("Connection failed: " . $conn->connect_error);
  }
?>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Simple Recorder.js demo with record, stop and pause</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <h1>Sai Estate Audio Recorder </h1>
    <div id="controls">
      <button id="recordButton" disabled>Record</button>
      <button id="pauseButton" disabled>Pause</button>
      <button id="stopButton" disabled>Stop</button>
    
    </div>
    <br>
    <br>
    <h3>Select User</h3>
    <!-- Displaying user name from database -->
    <?php
      $sql = "SELECT caller_id FROM callers";
      $result = mysqli_query($conn, $sql);
      echo "<select id='nameBox' name='caller_id'>";
      while ($row = mysqli_fetch_array($result)) 
      {
        echo "<option value='" . $row['caller_id'] ."'>" . $row['caller_id'] ."</option>";
      }
      echo "</select>";
      $name="<script>document.writeln(document.getElementById('nameBox').value);</script>";
    ?>

    <br>
    <br>
    <h3>Select Word</h3>
    <!-- Dislaying word from database -->
    <?php
      $sql = "SELECT word FROM key_words";
      $result = mysqli_query($conn, $sql);
      echo "<select id='textBox' name='word'>";
      while ($row = mysqli_fetch_array($result)) 
      {
        echo "<option value='" . $row['word'] ."'>" . $row['word'] ."</option>";
      }
      echo "</select>";
    ?>
      
    <br>    
    <div id="formats">Format: start recording to see sample rate</div>
  	<h3>Recordings</h3>
  	<ol id="recordingsList"></ol>

    <!-- inserting these scripts at the end to be able to use all the elements in the DOM -->
  	<script src="https://cdn.rawgit.com/mattdiamond/Recorderjs/08e7abd9/dist/recorder.js"></script>
  	<script src="js/app.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
  </body>
</html>