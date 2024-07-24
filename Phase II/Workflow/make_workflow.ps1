$yw = "D:\sandbox\CS513\yw-idcc-17\yw_jar\yesworkflow-0.2.0-jar-with-dependencies.jar"

java -jar $yw graph menu_cleaning_outer_workflow-v2.py -config graph.view=combined -config graph.layout=tb -config graph.portlayout=relax > .\menu_cleaning_outer_workflow-v2.gv

dot -Tpdf .\menu_cleaning_outer_workflow-v2.gv -o menu_cleaning_outer_workflow-v2.pdf

dot -Tsvg .\menu_cleaning_outer_workflow-v2.gv -o menu_cleaning_outer_workflow-v2.svg

dot -Tpng .\menu_cleaning_outer_workflow-v2.gv -o menu_cleaning_outer_workflow-v2.png
