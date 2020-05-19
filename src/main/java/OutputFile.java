import java.io.File;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.ArrayList;

public class OutputFile {
   String tabNumber;
   List<String[]> dataLines = new ArrayList<>();
   File csvOutputFile;

   public OutfileFile(String tab) {
      tabNumber = tab;
      String fileName = "tab_" + tab + ".csv";

      this.csvOutputFile = new File(fileName);
   }

   public void addValue(String time, String x, String y) {
      List<String[]> dataLines = new ArrayList<>();
      dataLines.add(new String[] {time, x, y});

      //this.csvOutputFile.write();
   }

   private String convertToCSV(String[] data) {
      return Stream.of(data)
        //.map(this::escapeSpecialCharacters)
        .collect(Collectors.joining(","));
  }
}