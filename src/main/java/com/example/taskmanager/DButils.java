package com.example.taskmanager;

import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.*;

public class DButils {
    public static void changeScene(ActionEvent event, String fmxlFile, String title, String user) {
        Parent root = null;

        if (user != null){
            try{
                FXMLLoader loader = new FXMLLoader(DButils.class.getResource(fmxlFile));
                root = loader.load();
                LoggedInController loggedInController = loader.getController();
            } catch (IOException e) {
                e.printStackTrace();
            }
        } else {
            try{
                root = FXMLLoader.load(DButils.class.getResource(fmxlFile));
            } catch (IOException e){
                e.printStackTrace();
            }
        }
        Stage stage = (Stage)((Node) event.getSource()).getScene().getWindow();
        stage.setTitle(title);
        stage.setScene(new Scene(root, 600, 400));
        stage.show();
    }

    public static void signUpUser(ActionEvent event, String user, String pass) {
        Connection connection = null;
        PreparedStatement psInsert = null;
        PreparedStatement psCheckUserExists = null;
        ResultSet resultSet = null;
        try{
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/taskManagement", "root", "P@ssw0rd");
            psCheckUserExists = connection.prepareStatement("select * from user where name=? ");
            psCheckUserExists.setString(1, user);
            resultSet = psCheckUserExists.executeQuery();

            if(resultSet.isBeforeFirst()){
                System.out.println("User already exists");
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setContentText("You cannot use this username");
                alert.show();
            } else {
                psInsert = connection.prepareStatement("insert into user (name, password) values(?,?)");
                psInsert.setString(1, user);
                psInsert.setString(2, pass);
                psInsert.executeUpdate();

                changeScene(event, "logged-in.fxml", "Task Manager", "User");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (resultSet != null) {
                try {
                    resultSet.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (psInsert != null) {
                try {
                    psInsert.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (connection != null) {
                try {
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void logInUser(ActionEvent event, String user, String pass) {

        Connection connection = null;
        PreparedStatement preparedStatement = null;
        ResultSet resultSet = null;
        try{
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/taskManagement", "root", "P@ssw0rd");
            preparedStatement = connection.prepareStatement("select password from user where name=? ");
            preparedStatement.setString(1, user);
            resultSet = preparedStatement.executeQuery();

            if(!resultSet.isBeforeFirst()){
                System.out.println("User not found");
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setContentText("Provided credential corrects");
                alert.show();
            } else {
                while(resultSet.next()){
                    String retrievedPassword = resultSet.getString("password");
                    if (retrievedPassword.equals(pass)) {
                        changeScene(event, "logged-in.fxml", "Task Manager", "User");
                    } else {
                        System.out.println("Wrong password");
                        Alert alert = new Alert(Alert.AlertType.ERROR);
                        alert.setContentText("Wrong password");
                        alert.show();
                    }

                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        } finally {
            if (resultSet != null) {
                try {
                    resultSet.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (preparedStatement != null) {
                try {
                    preparedStatement.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if (connection != null) {
                try {
                    connection.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }

    }
}
