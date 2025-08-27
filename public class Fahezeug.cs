public class Fahezeug
{
    public String Motor;
    public int Reifen;
    public String Farbe;


    public Fahrzeug()
    {
        Motor = "Diesel";
        Reifen = 4;
        Farbe = "Rot";
    }
    public void Lenken()
    {

    }
    public void Fahren()
    {

    }

}


public class Panzer
{
    public int Panzerung;
    public String Bewaffnung;
    public int Munition;

    public Panzer()
    {
        Panzerung = 100;
        Bewaffnung = "10,5,mm Pak";schießen
        Munition = 200;
    }

    public void schießen
    {
        Munition = Munition - 1;
    }



}