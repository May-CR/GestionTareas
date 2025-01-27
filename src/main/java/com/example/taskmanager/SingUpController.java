package com.example.taskmanager;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;


import java.net.URL;
import javafx.scene.control.TextField;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import java.util.ResourceBundle;

public class SingUpController implements Initializable {

    @FXML
    private TextField tf_user;
    @FXML
    private TextField tf_password;
    @FXML
    private Button button_sign_up;
    @FXML
    private Button button_return;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        button_sign_up.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                if (!tf_user.getText().trim().isEmpty() && !tf_password.getText().trim().isEmpty()) {
                    DButils.signUpUser(event, tf_user.getText(), tf_password.getText());
                } else {
                    System.out.println("Please fill in all information");
                    Alert alert = new Alert(Alert.AlertType.ERROR);
                    alert.setContentText("Please fill in all information");
                    alert.show();
                }
            }
        });

        button_return.setOnAction(new  EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                DButils.changeScene(event, "login.fxml", "Task Manager", null);

            }
        });
    }
}
