import React, { useState } from "react";
import { useMutation, gql } from '@apollo/client';

const GET_NOTIFICATIONS = gql`
  query GetNotifications {
    notifications {
      id
      message
      timePosted
    }
  }
`;

const CREATE_NOTIFICATION = gql`
  mutation CreateNotification($message: String!) {
    createNotification(message: $message) {
      notification {
        id
        message
        timePosted
      }
    }
  }
`;

const Notifications = () => {
    const [notification, setNotification] = useState("");
    const [createNotification] = useMutation(CREATE_NOTIFICATION, {
        refetchQueries: [{ query: GET_NOTIFICATIONS }]  // Changed this line
    });

    const handleSendNotification = async () => {
        if (!notification.trim()) return;

        try {
            await createNotification({
                variables: { message: notification }
            });
            setNotification(""); // Clear input after sending
        } catch (error) {
            console.error("Error sending notification:", error);
        }
    };

    return (
        <div className="card notification-section">
            <h2>Send Notification</h2>
            <textarea
                placeholder="Enter notification message"
                value={notification}
                onChange={(e) => setNotification(e.target.value)}
            />
            <button onClick={handleSendNotification}>Send Notification</button>
        </div>
    );
};

export default Notifications;
