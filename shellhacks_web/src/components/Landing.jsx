import { TextField } from "@mui/material";
import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";

const path = "http://127.0.0.1:5000/";

function Landing() {
  const navigate = useNavigate();
  const [topic, setTopic] = useState("");

  return (
    <div>
      <h2>Landing Page</h2>

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
          style={{
            marginLeft: 8,
            height: 32,
          }}
          onClick={async () => {
            await axios.post(
              // navigate("/quiz");
              `${path}/topic`,
              {
                topic: topic,
              },
              {
                headers: {
                  //   Authorization: "Bearer " + localStorage.getItem("token"),
                },
              }
            );
          }}
        >
          LET'S GO
        </Button>
      </div>
    </div>
  );
}

export default Landing;
