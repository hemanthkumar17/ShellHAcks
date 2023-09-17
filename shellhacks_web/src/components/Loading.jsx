import { CircularProgress } from "@mui/material";

export const Loading = () => {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        width: "100%",
        marginTop: "30px",
      }}
    >
      <div style={{ display: "flex", justifyContent: "center" }}>
        <CircularProgress />
      </div>
    </div>
  );
};
