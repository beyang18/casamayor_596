import 'package:flutter/material.dart';
import 'package:modelhandling/screens/login_screen.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

void main()async {
  WidgetsFlutterBinding.ensureInitialized( );
  await Supabase.initialize(url: "https://kqbaswsgfxvjbelyfoga.supabase.co", anonKey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtxYmFzd3NnZnh2amJlbHlmb2dhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzA4ODQzMjYsImV4cCI6MjA4NjQ2MDMyNn0.e9_zG-9kGOzgB6MV9ZGpYcKF0O_9UdXfLFtuyw_eUlI");



  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(    
        colorScheme: .fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const LoginPage(),
    );
  }
}
