import java.util.ArrayList;

public class Program{
    public static void main(String[] args){
        //sets up pseudo database of shapes
        ArrayList<Shape> database = new ArrayList<Shape>();
        
        database.add(new Square());
        database.add(new Triangle());
        database.add(new Triangle());
        database.add(new Circle());
        database.add(new Triangle());
        database.add(new Square());
        database.add(new Square());
        database.add(new Triangle());
        database.add(new Circle());
        database.add(new Circle());
        database.add(new Square());
        database.add(new Triangle());
        database.add(new Square());

        int numShapes = database.size();
        System.out.println("Database contains " + numShapes + " shapes");

        for (Shape shape : database){
            shape.display();
        }
}
}