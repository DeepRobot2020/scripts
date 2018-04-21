import json
import pdb
import matplotlib.pyplot as plt


pipeline1_bitrate_config = []
pipeline2_bitrate_config = []

pipeline1_bitrate_actual = []
pipeline2_bitrate_actual = []


ABR_BR = []
with open("log.blog.JSON", "r") as file:
        for i, line in enumerate(file):

            line_dict = json.loads(line)
            if i == 0:
                print("\nLog Header\n{0}\n{1}".format("-" * 6, line_dict))
            elif i == 1:
                print("\nLog Meta\n{0}\n{1}".format("-" * 6, line_dict))
            elif i == 2:
                print("\nLog Schema\n{0}\n{1}".format("-" * 6, line_dict))
            else:
                if line_dict['name'] == 'CAM_STREAMING_STATS':
                    br_actual_sum = sum(line_dict['payload']['enc_bps'])
                    br_config_sum = sum(line_dict['payload']['enc_config_bps'])
                    br_abr = int(line_dict['payload']['abr_throughput']) * 8 * 3 / 4
                    # ABR_BR.append(br_abr)

                    if int(line_dict['payload']['pipeline_id']) == 0:
                        pipeline1_bitrate_config.append(br_config_sum)
                        pipeline1_bitrate_actual.append(br_actual_sum)
                    else:
                        pipeline2_bitrate_config.append(br_config_sum)
                        pipeline2_bitrate_actual.append(br_actual_sum)
                        ABR_BR.append(br_abr)

                #process_message(line_dict)

# import pdb; pdb.set_trace()

plt.plot(pipeline2_bitrate_config, label='Total encoder config bitrate')
plt.plot(pipeline2_bitrate_actual, label='Total encoder actual bitrate')
plt.plot(ABR_BR, label='ABR bitrate (x 0.75)')


plt.legend()
plt.show()

