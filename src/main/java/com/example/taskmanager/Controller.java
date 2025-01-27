package com.example.taskmanager;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

import java.net.URL;
import java.util.ResourceBundle;

public class Controller  implements Initializable {

    @FXML
    private Button button_join;
    @FXML
    private TextField tf_user;
    @FXML
    private TextField tf_pass;
    @FXML
    private Button button_sign_up;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

        button_join.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                DButils.logInUser(event, tf_user.getText(), tf_pass.getText());
            }
        });

        button_sign_up.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                DButils.changeScene(event, "sign-up.fxml", "Task Manager", null);
            }
        });

    }
}