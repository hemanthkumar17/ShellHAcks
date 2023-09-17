import { Button } from "@mui/material";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { useState } from "react";
import "../landing.css";
import { useCallback } from "react";
import Particles from "react-tsparticles";
import { loadFull } from "tsparticles";
import particlesConfig from "../config/particlesConfig";
import { Loading } from "./Loading";

const path = "http://127.0.0.1:5000";

function myFunction() {
  var element = document.body;
  var element2 = document.getElementsByClassName("topic-button");
  var element3 = document.getElementsByClassName("toggle-button");
  element2 = element2[0];
  element3 = element3[0];
  element.classList.toggle("dark-mode");
  element2.classList.toggle("dark-mode");
  element3.classList.toggle("icon-night-dark");
}

function Landing() {
  const navigate = useNavigate();
  const [topic, setTopic] = useState("");
  const [load, setLoad] = useState(false);
  const particlesInit = useCallback(async (engine) => {
    console.log(engine);
    // you can initiate the tsParticles instance (engine) here, adding custom shapes or presets
    // this loads the tsparticles package bundle, it's the easiest method for getting everything ready
    // starting from v2 you can add only the features you need reducing the bundle size
    //await loadFull(engine);
    await loadFull(engine);
  }, []);

  const particlesLoaded = useCallback(async (container) => {
    await console.log(container);
  }, []);

  return (
    <div>
      {/* <div style={{ position: "absolute" }}>
        <Particles height="100vh" width="100vw" params={particlesConfig} />
      </div> */}

      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <h2>SmartTrail: Personalized Learning Journeys for All</h2>

        <div
          style={{
            display: "flex",
            flexDirection: "column",
          }}
        >
          <input
            type="text"
            placeholder="Topic to Learn"
            class="text-field"
            onChange={(e) => setTopic(e.target.value)}
          />
          {/* <div className="button-div"> */}
          <Button
            style={{
              marginTop: 8,
            }}
            variant="contained"
            // class="topic-button"
            onClick={async () => {
              if (topic.trim === "") {
                return;
              }
              
              setLoad(true)
              const response = await axios.post(
                `${path}/topic`,
                {
                  topic: topic,
                },
                {
                  headers: {
                    "Content-Type": "application/json",
                  },
                }
              );
              setLoad(false)
              if (response.status != 200) {
                throw new Error("Request failed");
              } else {
                navigate("/quiz");
              }
            }}
            disabled={!topic.trim()}
          >
            LET'S GO
          </Button>
          {load === true ? <Loading /> : null}
          {/* </div> */}
        </div>
      </div>
    </div>
  );
}

export default Landing;
