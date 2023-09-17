import * as React from "react";
import Box from "@mui/material/Box";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import { useNavigate } from "react-router-dom";
import { useEffect } from "react";

export default function CenteredTabs() {
  const [value, setValue] = React.useState(0);

  const navigate = useNavigate("");
  const handleChange = (event, newValue) => {
    console.log(newValue);
    if (newValue == 0) {
      navigate("/answers");
    } else {
      navigate("/learn");
    }
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%", bgcolor: "background.paper" }}>
      <Tabs value={value} onChange={handleChange} centered>
        <Tab label="Practice Questions" />
        <Tab label="Video Lectures" />
      </Tabs>
    </Box>
  );
}
