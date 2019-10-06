
Sub Stock_Data():

'Declare Variables for WorkSheet

 Dim ws As Worksheet
 Dim ws_count As Integer
 Dim last_row As Double

'Declear variables for Consolidated rows for ticker symbol with their total volume.

 Dim ticker_row As Integer
 Dim total_volume As Double

'Declear variables for calculating Yearly Change and percentage.

 Dim open_value As Double
 Dim close_vale As Double
 Dim yearly_change As Double
 Dim change_percentage As Double

'Declear Variables for Percentage Increase,  Percentage Decrease and  Stock Volume.

 Dim percentage_inc As Double
 Dim percentage_dec As Double
 Dim stock_volume As Double
 
'Count number sheets for Current Workbook

 ws_count = ActiveWorkbook.Worksheets.Count

'Use Loop to go through each Worksheet.
  
    For Each ws In Worksheets
     
'Set Headings for each Sheet.
    
     ws.Cells(1, 9).Value = "Ticker"
     ws.Cells(1, 10).Value = "Yearly Change"
     ws.Cells(1, 11).Value = "Percent Change"
     ws.Cells(1, 12).Value = "Total Stock Volume"
     ws.Cells(2, 15).Value = "Greatest % Increase"
     ws.Cells(3, 15).Value = "Greatest % Decrease"
     ws.Cells(4, 15).Value = "Greatest Total Volume"
     ws.Cells(1, 16).Value = "Ticker"
     ws.Cells(1, 17).Value = "Value"
     open_value = ws.Cells(2, 3)
	 
'Set initial values for Stock volume, Ticker Symbol Row, Increase Decrease percent and stock volume.
    
     ticker_row = 2
     total_volume = 0
     stock_volume = 0
     percentage_inc = 0
     percentage_dec = 0
 
'Get count of last row for every sheet.
    
 last_row = Cells(Rows.Count, 1).End(xlUp).Row
      
'Looping each row of the sheet.

        For i = 2 To last_row
                                 
          If (ws.Cells(i, 1).Value = ws.Cells(i + 1, 1).Value) Then
              total_volume = total_volume + ws.Cells(i, 7).Value
        
             If (open_value = 0) Then
                 open_value = ws.Cells(i + 1, 3).Value
            End If
                
'Condition for all data related to one Ticker is consolidated and found a new Ticker Symbol in next row.
          
          Else
              total_volume = total_volume + ws.Cells(i, 7).Value
              ws.Cells(ticker_row, 9).Value = ws.Cells(i, 1).Value
                                
              close_value = ws.Cells(i, 6).Value
                    
'Calculate yearly change between stock's
            
               yearly_change = (close_value - open_value)
               ws.Cells(ticker_row, 10).Value = yearly_change
               
'Formatting for yearly_change
               
               If (ws.Cells(ticker_row, 10).Value > 0) Then
                   ws.Cells(ticker_row, 10).Interior.ColorIndex = 4
                   
               ElseIf (ws.Cells(ticker_row, 10).Value < 0) Then
                   ws.Cells(ticker_row, 10).Interior.ColorIndex = 3
             
               ElseIf (ws.Cells(ticker_row, 10).Value = 0) Then
                   ws.Cells(ticker_row, 10).Interior.ColorIndex = 0
               
               End If
               
'Exception handling for stock value with "0".
            
               If (open_value = 0) Then
                   ws.Cells(ticker_row, 11).Value = 0
        
               Else
                   change_percentage = (yearly_change / open_value) * 100
                   ws.Cells(ticker_row, 11).Value = change_percentage
                   ws.Cells(ticker_row, 11).Value = Round(change_percentage, 2)
                   ws.Cells(ticker_row, 11).NumberFormat = "0.00\%"
               End If
                           
'Formatting for change_percentage
               
               If (ws.Cells(ticker_row, 11).Value > 0) Then
                   ws.Cells(ticker_row, 11).Interior.ColorIndex = 4
                   
               ElseIf (ws.Cells(ticker_row, 10).Value < 0) Then
                   ws.Cells(ticker_row, 11).Interior.ColorIndex = 3
             
               ElseIf (ws.Cells(ticker_row, 10).Value = 0) Then
                   ws.Cells(ticker_row, 11).Interior.ColorIndex = 0
               
               End If
            
'Condition to pick percentage increase.
            
                If (ws.Cells(ticker_row, 11).Value > percentage_inc) Then
                    ws.Cells(2, 16).Value = ws.Cells(ticker_row, 9).Value
                    ws.Cells(2, 17).Value = ws.Cells(ticker_row, 11).Value
                    percentage_inc = ws.Cells(ticker_row, 11).Value
                    ws.Cells(2, 17).NumberFormat = "0.00\%"
            
                End If
            
'Condition to pick percent decrease.
            
                If (ws.Cells(ticker_row, 11).Value < percentage_dec) Then
                    ws.Cells(3, 16).Value = ws.Cells(ticker_row, 9).Value
                    ws.Cells(3, 17).Value = ws.Cells(ticker_row, 11).Value
                    percentage_dec = ws.Cells(ticker_row, 11).Value
                    ws.Cells(3, 17).NumberFormat = "0.00\%"
                
                End If
            
'Writing total stock volume for a stock in loop.
            
                ws.Cells(ticker_row, 12).Value = total_volume
             
'Condition to pick maximum stock total volume
                
                If (ws.Cells(ticker_row, 12).Value > stock_volume) Then
                    ws.Cells(4, 16).Value = ws.Cells(ticker_row, 9)
                    ws.Cells(4, 17).Value = ws.Cells(ticker_row, 12)
                    stock_volume = ws.Cells(ticker_row, 12).Value
            
                End If
            
'Pointing to next desired row where my next iteration writes data.
            
                ticker_row = ticker_row + 1
            
'Resetting stock total value to "0" and setting initial reading value for next iteration
            
     			total_volume = 0
                open_value = ws.Cells(i + 1, 3)
            
            End If

        Next i

    Next
   
End Sub



