package com.example.taskmanager;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;

import java.net.URL;
import java.util.ResourceBundle;

public class LoggedInController implements Initializable {

    @FXML
    private Button button_LogOut;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        button_LogOut.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                DButils.changeScene(event, "login.fxml", "Task Manager", null);
            }
        });

    }


}
