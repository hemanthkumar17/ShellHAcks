import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import { useEffect, useState } from "react";
import axios from "axios";
import { BASE_URL } from "../config";
import { Loading } from "./Loading";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import CenteredTabs from "./Tabs";

function Answer() {
  const [qanda, setqanda] = useState([]);

  useEffect(() => {
    async function getQandA() {
      const response = await axios.get(`${BASE_URL}/practiceqa`, {}, {});

      if (!response.status == 200) {
        throw new Error("Request failed");
      } else {
        setqanda(response.data.questions.questions);
      }
    }
    getQandA();
  }, []);

  return (
    <div
      style={{
        height: "100%",
      }}
    >
      <CenteredTabs />
      <h2
        style={{
          textAlign: "center",
        }}
      >
        "Q&A Unleashed"
      </h2>
      <Box
        sx={{
          width: "100%",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <Grid
          container
          rowSpacing={1}
          columnSpacing={{ xs: 1, sm: 2, md: 3 }}
          style={{
            display: "flex",
            justifyContent: "center",
            alignContent: "center",
          }}
        >
          {qanda.length > 0 ? <SetQandA questions={qanda} /> : <Loading />}
        </Grid>
      </Box>
    </div>
  );
}

function SetQandA({ questions }) {
  {
    return questions[0].map((item) => {
      return (
        <Grid item xs={6}>
          <Card sx={{ maxWidth: 345, height: "100%" }}>
            <CardContent>
              <Typography
                gutterBottom
                variant="h5"
                component="div"
                style={{
                  color: "#0072bb",
                }}
              >
                {item.question}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {item.answer}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      );
    });
  }
}

export default Answer;
