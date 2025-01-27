 package com.example.taskmanager;

import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class Application extends javafx.application.Application {
    @Override
    public void start(Stage stage) throws IOException {
        /*FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("login.fxml"));
        Scene scene = new Scene(fxmlLoader.load());
        stage.setScene(scene);
        stage.show();*/

        Parent root = FXMLLoader.load(getClass().getResource("login.fxml"));
        stage.setTitle("Task Manager");
        stage.setScene(new Scene(root, 600, 400));
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}