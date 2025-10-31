import React, { useState } from "react";
import Sidebar from "./components/Sidebar";
import SendEmail from "./components/SendEmail";
import ReplyEmail from "./components/ReplyEmail";
import ForwardEmail from "./components/ForwardEmail";
import ViewThread from "./components/ViewThread";
import ViewEmails from "./components/ViewEmails";
import ViewClusters from "./components/ViewClusters";  

export default function App() {
  const [view, setView] = useState("send");

  const renderView = () => {
    switch (view) {
      case "send":
        return <SendEmail />;
      case "reply":
        return <ReplyEmail />;
      case "forward":
        return <ForwardEmail />;
      case "viewThread":
        return <ViewThread />;
      case "viewEmails":
        return <ViewEmails />;
      case "viewClusters":                     
        return <ViewClusters />;
      default:
        return <SendEmail />;
    }
  };

  return (
    <div style={{ display: "flex" }}>
      <Sidebar setView={setView} />
      <div style={{ padding: "20px", flex: 1 }}>
        {renderView()}
      </div>
    </div>
  );
}

