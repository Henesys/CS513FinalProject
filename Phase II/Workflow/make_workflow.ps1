$yw = "D:\sandbox\CS513\yw-idcc-17\yw_jar\yesworkflow-0.2.0-jar-with-dependencies.jar"

java -jar $yw graph menu_cleaning_outer_workflow.py -config graph.view=combined -config graph.layout=tb -config graph.portlayout=relax > .\menu_cleaning_outer_workflow.gv

dot -Tpdf .\menu_cleaning_outer_workflow.gv -o menu_cleaning_outer_workflow.pdf

dot -Tsvg .\menu_cleaning_outer_workflow.gv -o menu_cleaning_outer_workflow.svg