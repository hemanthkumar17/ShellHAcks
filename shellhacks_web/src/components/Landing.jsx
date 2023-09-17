import { TextField } from "@mui/material";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";
import '../landing.css'
// import {} from '@material-ui/icons';
import ModeNightIcon from '@mui/icons-material/ModeNight';
import LightModeIcon from '@mui/icons-material/LightMode';
const path = "http://127.0.0.1:5000";

function myFunction() {
  var element = document.body;
  var element2 = document.getElementsByClassName("topic-button"); 
  var element3 = document.getElementsByClassName("toggle-button"); 
  element2=element2[0];
  element3=element3[0];
  element.classList.toggle("dark-mode");
  element2.classList.toggle("dark-mode");
  element3.classList.toggle("icon-night-dark");
}

function Landing() {
  const navigate = useNavigate();
  const [topic, setTopic] = useState("");

  return (
    <div>
      <h2>SmartTrail: Personalized Learning Journeys for All</h2>

      <div>
        <TextField
          id="outlined-basic"
          label="Enter the topic of your choice"
          variant="outlined"
          onChange={(e) => setTopic(e.target.value)}
          style={{
            height: 32,
          }}
        />
        <Button
          variant="contained"
          class="topic-button"
          onClick={async () => {
            const response = await axios.post(
              // navigate("/quiz");
              `${path}/topic`,
              {
                topic: topic,
              },
              {
                headers: {
                  //   Authorization: "Bearer " + localStorage.getItem("token"),
                  "Content-Type": "application/json",
                },
              }
            );

            console.log(response);
            if (response.status != 200) {
              throw new Error("Request failed");
            } else {
              navigate("/quiz");
            }
          }}
        >
          LET'S GO
        </Button>
        <Button class="toggle-button" onClick={myFunction}>
            <ModeNightIcon >Tog</ModeNightIcon>
        </Button>
      </div>
    </div>
  );
}

export default Landing;
