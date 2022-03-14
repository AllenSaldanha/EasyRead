import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

import './main.dart';

// Future recognizer() async {
//     var response = await http.get(Uri.parse('http://127.0.0.1:5000/predict'));
//     print(response.body);
//   }

class Recognized extends StatelessWidget {
  final String recognizedContent;
  Recognized(this.recognizedContent);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Recognized Content'),
      ),
      body: Container(
        child: Column(
          children: [
            Text(recognizedContent),
            ElevatedButton(
              onPressed: () => Navigator.pop(context),
              child: Text('Click to go back'),
            ),
          ],
        ),
      ),
    );
  }
}
