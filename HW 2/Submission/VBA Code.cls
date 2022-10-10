Sub Stonck_Challenge()

   
Dim ticker As String
Dim start_of_year As Double
Dim end_of_year As Double
Dim annual_change As Double
Dim total_stock_volume As Double
 
'row titles
Range("J1").Value = "ticker"
Range("K1").Value = "yearly_change"
Range("L1").Value = "percentage_change"
Range("M1").Value = "total_stock_volume"

'variables/dimensions
table_row = 2
end_of_year = 0
yearly_change = 0
percentage_change = 0
total_stock_volume = 0
start_of_year = Range("C2").Value
the_last_row = Cells(Rows.Count, 1).End(xlUp).Row

'for loop goes through each row of data-set
 For i = 2 To the_last_row

'if the cells are different then go to else
If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

total_stock_volume = total_stock_volume + Cells(i, 7).Value

  'add ticker
 ticker = Cells(i, 1).Value
  
'find the yearly change
end_of_year = Range("F" & i).Value

yearly_change = end_of_year - start_of_year

'percentage change
percentage_change = yearly_change / start_of_year

percentage_change = Format(percentage_change, "0.00%")

start_of_year = Cells(i + 1, 3).Value

Range("J" & table_row).Value = ticker

Range("K" & table_row).Value = yearly_change

Range("L" & table_row).Value = percentage_change

Range("M" & table_row).Value = total_stock_volume

table_row = table_row + 1

total_stock_volume = 0

 Else

total_stock_volume = total_stock_volume + Cells(i, 7).Value


 End If

 Next i

 For i = 2 To the_last_row

If Range("K" & i) > 0 Then

Range("K" & i).Interior.ColorIndex = 4

ElseIf Range("K" & i) < 0 Then
Range("K" & i).Interior.ColorIndex = 3

Else
Range("K" & i).Interior.ColorIndex = 2

               
End If

  Next i
        

        

    End Sub

